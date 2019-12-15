from concurrent import futures
import grpc
import proto.master_pb.master_pb2 as master_pb2
import proto.master_pb.master_pb2_grpc as master_pb2_grpc
import proto.volume_pb.volume_pb2 as volume_pb2
import proto.volume_pb.volume_pb2_grpc as volume_pb2_grpc
import zmq
import mysql.connector
import sys
import os
from datetime import datetime

FILE_PORT = 5002
CHUNK_SIZE = 1000

class MasterServer(master_pb2_grpc.MasterNodeServicer):
    def __init__(self, args=None):
        self.options = {}
        self.cur_volume_id = 0
        # map of volume_id to its grpc_port
        self.volumes = {}
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
        )
        self.name = args.name
        self.createDB(self.name)

    # Create Metadata Database
    def createDB(self, name):
        mycursor = self.mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS filesystem")
        mycursor.execute("USE filesystem")
        mycursor.execute("DROP TABLE IF EXISTS %s" % name)
        mycursor.execute("CREATE TABLE %s (" % name
                + "path VARCHAR(255), volumeId INT, size INT, date DATETIME)")
        mycursor.close()

    # gRPC method to inform master of a newly added volume
    # master will returns an incrementing volume id 
    # TODO: better id generation scheme to take into account revived volumes
    def AddVolume(self, request, context):
        self.volumes[self.cur_volume_id] = request.volume_grpc
        self.cur_volume_id += 1
        return master_pb2.AddVolumeResponse(
            response_code=master_pb2.AddVolumeResponse.AddVolumeResponseCode.Value('success'),
            volume_id=(self.cur_volume_id - 1)
        )

    # gRPC method to upload a file to a volume
    # assign volume by least used policy (i.e volume with lowest used space will be chosen)
    def Upload(self, request, context):
        # assign volume for this upload request based on used space
        min_used = sys.maxsize
        min_volume = -1
        for volume_id, grpc_addr in self.volumes.items():
            with grpc.insecure_channel(grpc_addr) as channel:
                volume_client = volume_pb2_grpc.VolumeNodeStub(channel)
                resp = volume_client.GetUsedSpace(volume_pb2.GetUsedSpaceRequest())
                if resp.used_space < min_used:
                    min_used = resp.used_space
                    min_volume = resp.volume_id
       
        # split file to chunks and send to volume node
        path = request.file_path
        file = open(path, "rb")
        chunks_iterator = self._generate_chunks(file, path)

        with grpc.insecure_channel(self.volumes[min_volume]) as channel:
            volume_client = volume_pb2_grpc.VolumeNodeStub(channel)
            resp = volume_client.WriteFile(chunks_iterator)
        
        # remove the temp file
        os.remove(path)

        # insert into the metadata
        cursor = self.mydb.cursor()
        cursor.execute("USE filesystem")
        sql = "INSERT INTO %s (path, volumeId, size, date) VALUES (\"%s\", %s, %s, NOW())" % (self.name, path, "%d" % min_volume, "%d" % request.file_size)
        cursor.execute(sql)
        cursor.close()

        self.mydb.commit()

        resp = master_pb2.UploadResponse(
            volume_id=min_volume
        )
        return resp

    # helper method to generate WriteFileChunk iterable request for gRPC method WriteFile in volume
    def _generate_chunks(self, file, path):
        while True:
            data = file.read(CHUNK_SIZE)
            chunk = volume_pb2.WriteFileChunk(
                path=path,
                content=data,
                length=len(data)
            )
            if not data:
                break
            yield chunk
            
def serve(args):
    grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    master_pb2_grpc.add_MasterNodeServicer_to_server(MasterServer(args), grpc_server)
    grpc_addr = '{ip}:{port}'.format(ip=args.ip, port=args.grpc_port)
    grpc_server.add_insecure_port(grpc_addr)
    grpc_server.start()
    grpc_server.wait_for_termination()


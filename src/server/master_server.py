from concurrent import futures
import grpc
import proto.master_pb.master_pb2 as master_pb2
import proto.master_pb.master_pb2_grpc as master_pb2_grpc
import proto.volume_pb.volume_pb2 as volume_pb2
import proto.volume_pb.volume_pb2_grpc as volume_pb2_grpc
import zmq
import mysql.connector

FILE_PORT = 5002

class MasterServer(master_pb2_grpc.MasterNodeServicer):
    def __init__(self, args=None):
        self.options = {}
        
        # map of volume_id to its grpc_port
        self.volumes = {}

    def AddVolume(self, request, context):
        if request.volume_id in self.volumes:
            return master_pb2.AddVolumeResponse(
                response_code=master_pb2.AddVolumeResponse.AddVolumeResponseCode.Value('duplicate_id')
            )
        else:
            self.volumes[request.volume_id] = request.volume_grpc
            return master_pb2.AddVolumeResponse(
                response_code=master_pb2.AddVolumeResponse.AddVolumeResponseCode.Value('success')
            )

    def Upload(self, request, context):
        pass
            
def serve(args):
    grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    master_pb2_grpc.add_MasterNodeServicer_to_server(MasterServer(args), grpc_server)
    grpc_addr = '{ip}:{port}'.format(ip=args.ip, port=args.grpc_port)
    grpc_server.add_insecure_port(grpc_addr)
    grpc_server.start()
    grpc_server.wait_for_termination()

def createDB(name):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS filesystem")
    mycursor.execute("USE filesystem")
    mycursor.execute("DROP TABLE IF EXISTS %s" % name)
    mycursor.execute("CREATE TABLE %s (id INT AUTO_INCREMENT PRIMARY KEY, " % name
            + "path VARCHAR(255), volumeId INT, size INT)")

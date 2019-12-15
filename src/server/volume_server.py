from concurrent import futures
import grpc
import proto.volume_pb.volume_pb2 as volume_pb2
import proto.volume_pb.volume_pb2_grpc as volume_pb2_grpc
import os

class VolumeServer(volume_pb2_grpc.VolumeNodeServicer):
    def __init__(self, volume_id, args=None):
        self.used_space = 0
        self.id = volume_id
        self.dir_path = "/home/volumes/volume_%d" %self.id
        os.makedirs(self.dir_path, exist_ok=True)

    # gRPC method to get the currently used space by this volume
    # TODO: add logic to support delete/modify files
    def GetUsedSpace(self, request, context):
        resp = volume_pb2.GetUsedSpaceResponse(
            used_space=self.used_space,
            volume_id=self.id
        )
        return resp

    # gRPC method to write the file to this volume
    # accepts a stream/iterable request so we can write sequentially
    def WriteFile(self, request_iterator, context):
        cur_path = ""
        cur_file = None
        total_sent = 0
        total_written = 0

        for chunk in request_iterator:
            file_path = chunk.path
            full_path = os.path.join(self.dir_path, file_path)
            if full_path != cur_path:
                if cur_file is not None:
                    cur_file.close()
                cur_path = full_path
                cur_file = open(cur_path, "w")
            
            data = chunk.content
            cur_file.write(data.decode())
            total_written += len(data)
            total_sent += chunk.length
        
        if cur_file is not None:
            cur_file.flush()

        self.used_space += total_written

        if total_sent == total_written:
            return volume_pb2.WriteFileResponse(
                bytes_written=total_written,
                response_code=volume_pb2.WriteFileResponse.WriteStatusCode.Value('success')
            )
        else:
            return volume_pb2.WriteFileResponse(
                bytes_written=total_written,
                response_code=volume_pb2.WriteFileResponse.WriteStatusCode.Value('failed')
            )

def serve(volume_id, args):
        grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        volume_pb2_grpc.add_VolumeNodeServicer_to_server(VolumeServer(volume_id, args), grpc_server)
        grpc_addr = '{ip}:{port}'.format(ip=args.ip, port=args.grpc_port)
        grpc_server.add_insecure_port(grpc_addr)
        grpc_server.start()
        grpc_server.wait_for_termination()


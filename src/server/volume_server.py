from concurrent import futures
import grpc
import proto.volume_pb.volume_pb2 as volume_pb2
import proto.volume_pb.volume_pb2_grpc as volume_pb2_grpc

class VolumeServer():
    def __init__(self, args=None):
        self.options = {}
        self.grpc_addr = '{ip}:{port}'.format(ip=args.ip, port=args.grpc_port)
    
    def serve(self):
        grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        volume_pb2_grpc.add_VolumeNodeServicer_to_server(VolumeServicer(), grpc_server)
        grpc_server.add_insecure_port(self.grpc_addr)
        grpc_server.start()
        grpc_server.wait_for_termination()

class VolumeServicer(volume_pb2_grpc.VolumeNodeServicer):
    def __init__(self):
        pass


from concurrent import futures
import grpc
import proto.master_pb.master_pb2 as master_pb2
import proto.master_pb.master_pb2_grpc as master_pb2_grpc

class MasterServer():
    def __init__(self, args=None):
        self.options = {}
        self.grpc_addr = '{ip}:{port}'.format(ip=args.ip, port=args.grpc_port)
    
    def serve(self):
        grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        master_pb2_grpc.add_MasterNodeServicer_to_server(MasterServicer(), grpc_server)
        print(self.grpc_addr)
        grpc_server.add_insecure_port(self.grpc_addr)
        grpc_server.start()
        grpc_server.wait_for_termination()

class MasterServicer(master_pb2_grpc.MasterNodeServicer):
    def __init__(self):
        pass


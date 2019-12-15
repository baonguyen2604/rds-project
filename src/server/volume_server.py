from concurrent import futures
import grpc
import proto.volume_pb.volume_pb2 as volume_pb2
import proto.volume_pb.volume_pb2_grpc as volume_pb2_grpc

class VolumeServer(volume_pb2_grpc.VolumeNodeServicer):
    def __init__(self, args=None):
        self.used_space = 0

    def GetUsedSpace(self, request, context):
        resp = volume_pb2.GetUsedSpaceResponse(
            
        )

    def WriteFile(self, request_iterator, context):
        return super().WriteFile(request_iterator, context)

def serve(args):
        grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        volume_pb2_grpc.add_VolumeNodeServicer_to_server(VolumeServer(args), grpc_server)
        grpc_addr = '{ip}:{port}'.format(ip=args.ip, port=args.grpc_port)
        grpc_server.add_insecure_port(grpc_addr)
        grpc_server.start()
        grpc_server.wait_for_termination()


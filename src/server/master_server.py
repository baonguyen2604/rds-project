from concurrent import futures
import grpc
import proto.master_pb.master_pb2 as master_pb2
import proto.master_pb.master_pb2_grpc as master_pb2_grpc

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
            
def serve(args):
    grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    master_pb2_grpc.add_MasterNodeServicer_to_server(MasterServer(args), grpc_server)
    grpc_addr = '{ip}:{port}'.format(ip=args.ip, port=args.grpc_port)
    grpc_server.add_insecure_port(grpc_addr)
    grpc_server.start()
    grpc_server.wait_for_termination()


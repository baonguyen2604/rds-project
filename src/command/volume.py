from .command import Command
import proto.master_pb.master_pb2 as master_pb2
import proto.master_pb.master_pb2_grpc as master_pb2_grpc
import create_volume
import multiprocessing as mp
import grpc

class Volume(Command):
    name = "VolumeCommand"

    def __init__(self, args=None):
        Command.__init__(self, args)
        self.args = args

    def run(self):
        print("Volume command run")

        # Create a separate process to run volume
        process = mp.Process(target=create_volume.volume, args=(self.args,))
        process.start()

        # tell master about this new volume
        add_volume_request = master_pb2.AddVolumeRequest()
        with grpc.insecure_channel(self.args.master) as channel:
            master_client = master_pb2_grpc.MasterNodeStub(channel)
            master_client.AddVolume(add_volume_request)

        return "Started volume at %s:%d and GRPC port = %s" %(self.args.ip, self.args.port, self.args.grpc_port)


    @property
    def description(self):
        print("Volume description")
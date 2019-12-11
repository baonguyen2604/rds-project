import os
import proto.master_pb.master_pb2 as master_pb2
import proto.master_pb.master_pb2_grpc as master_pb2_grpc
from .command import Command

class Upload(Command):
    name = "UploadCommand"

    def __init__(self, args=None):
        Command.__init__(self, args)
        self.path = args.path
        self.files = {}

    def run(self):
        self._getAllFiles()
        self._submitFiles()

    @property
    def description(self):
        print("Upload description")
    
    def _getAllFiles(self):
        for root, dirs, files in os.walk(self.path):
            for filename in files:
                fullpath = os.path.join(root, filename)
                with open(fullpath, 'rb') as file:
                    file_content = file.read()
                    self.files[fullpath] = file_content

    def _submitFiles(self):
        assign_request = master_pb2.AssignRequest(
            count=len(self.files)
            )
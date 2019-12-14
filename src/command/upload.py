import os
import grpc
import proto.master_pb.master_pb2 as master_pb2
import proto.master_pb.master_pb2_grpc as master_pb2_grpc
from .command import Command
import zmq

FILE_PORT = 5002
class Upload(Command):
    name = "UploadCommand"

    def __init__(self, args=None):
        Command.__init__(self, args)
        self.path = args.path
        self.master_addr = args.master

    def run(self):
        message = self._downloadFiles()
        self._uploadFiles()
        return message

    @property
    def description(self):
        print("Upload description")
    
    def _downloadFiles(self):
        context = zmq.Context()
        subscriber = context.socket(zmq.SUB)
        subscriber.setsockopt(zmq.SUBSCRIBE, self.path.encode())
        subscriber.connect("tcp://127.0.0.1:%s" % FILE_PORT)
        totalSize = 0
        f = open(self.path, "w")

        while True:
            try:
                path, message = subscriber.recv_multipart()
            except zmq.ZMQError as e:
                # File upload failed
                f.close()
                os.remove(self.path)
                return "Failed"
                
            f.write(message.decode())
            size = len(message)
            totalSize += size
            if size == 0:
                break
        f.close()
        message = "File Successfully Uploaded: %d Bytes" % totalSize
        return message
            
    def _uploadFiles(self):
        upload_request = master_pb2.UploadRequest(
            file_path=self.path
            )
        
        with grpc.insecure_channel(self.master_addr) as channel:
            master_client = master_pb2_grpc.MasterNodeStub(channel)
            master_client.Upload(upload_request)
        

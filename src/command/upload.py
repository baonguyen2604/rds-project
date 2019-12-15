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
        self.fileSize = 0

    # first we download and store the files temporarily
    # then we request an upload from master with the path and size
    # master will take care of assigning the appropriate volume and send the file to that volume
    def run(self):
        message = self._downloadFiles()
        if message == "Failed":
            return message
        self._uploadFiles()
        return message

    @property
    def description(self):
        print("Upload description")
    
    # temporary download and store the file
    def _downloadFiles(self):
        context = zmq.Context()
        subscriber = context.socket(zmq.SUB)
        subscriber.setsockopt(zmq.SUBSCRIBE, self.path.encode())
        subscriber.connect("tcp://127.0.0.1:%s" % FILE_PORT)
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
            self.fileSize+= size
            if size == 0: # Reached end of file
                break
        f.close()
        message = "File Successfully Uploaded: %d Bytes" % self.fileSize
        return message
    
    # request master an upload with the current file path and size
    def _uploadFiles(self):
        upload_request = master_pb2.UploadRequest(
            file_size=self.fileSize,
            file_path=self.path
        )
        
        with grpc.insecure_channel(self.master_addr) as channel:
            master_client = master_pb2_grpc.MasterNodeStub(channel)
            master_client.Upload(upload_request)
        

import zmq
import pickle
from command.master import Master
from command.upload import Upload

SERVER_PORT = 5000

def DistributedFileSystem(args):
    command = None
    if args.command == 'master':
        command = Master(args)
    elif args.command == 'upload':
        command = Upload(args)
        
    command.run()
    

def FileSystemServer():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://127.0.0.1:%s" % SERVER_PORT)

    while True:
        message = socket.recv()
        args = pickle.loads(message)
        DistributedFileSystem(args)


if __name__ == '__main__':
    FileSystemServer()

import zmq
import pickle
from command.master import Master
from command.upload import Upload
from command.volume import Volume

SERVER_PORT = 5000

def DistributedFileSystem(args):
    command = None
    if args.command == 'master':
        command = Master(args)
    elif args.command == 'upload':
        command = Upload(args)
    elif args.command == 'volume':
        command = Volume(args)
        
    command.run()
    

def FileSystemServer():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:%s" % SERVER_PORT)

    while True:
        message = socket.recv()
        args = pickle.loads(message)
        DistributedFileSystem(args)


if __name__ == '__main__':
    FileSystemServer()

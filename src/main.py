import parser
from command.master import Master
from command.upload import Upload

def DistributedFileSystem(args):
    command = None
    if args.command == 'master':
        command = Master(args)
    elif args.command == 'upload':
        command = Upload(args)
        
    command.run()

if __name__ == '__main__':
    parser = parser.main_parser()
    args = parser.parse_args()

    DistributedFileSystem(args)
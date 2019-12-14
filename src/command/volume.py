from .command import Command

def Volume(Command):
    name = "VolumeCommand"

    def __init__(self, args=None):
        Command.__init__(self, args)
        self.options = {}
        self.options['ip'] = args.ip
        self.options['port'] = args.port
        self.options['grpc_port'] = args.grpc_port

    def run(self):
        print("Volume command run")

        # TODO: Create a separate process to run volume

    @property
    def description(self):
        print("Volume description")
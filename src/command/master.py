from .command import Command
import create_master
import multiprocessing as mp

class Master(Command):
    name = "MasterCommand"

    def __init__(self, args=None):
        Command.__init__(self, args)
        self.args = args

    def run(self):
        print("Master command run")

        # create different process to run master
        process = mp.Process(target=create_master.master, args=(self.args,))
        process.start()

        return "Started master at %s:%d and GRPC port = %s" %(self.args.ip, self.args.port, self.args.grpc_port)

    @property
    def description(self):
        print("Master description")

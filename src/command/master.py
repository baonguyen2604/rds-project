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

        # TODO: create different process to run master
        process = mp.Process(target=create_master.master, args=(self.args,))
        process.start()
        process.join()
        

    @property
    def description(self):
        print("Master description")

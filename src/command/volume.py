from .command import Command
import create_volume
import multiprocessing as mp

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
        process.join()

    @property
    def description(self):
        print("Volume description")
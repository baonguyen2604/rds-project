commands = [
    Master,
    Volume,
    Mount
]

class Command():
    name = "BaseCommand"

    def __init__(self, args):
        pass

    @property
    def run(self):
        pass

    @property
    def description(self):
        pass
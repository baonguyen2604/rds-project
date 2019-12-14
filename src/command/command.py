# commands = [
#     Master,
#     Volume,
#     Mount
# ]

class Command():
    name = "BaseCommand"

    def __init__(self, args):
        pass

    def run(self):
        return ""

    @property
    def description(self):
        pass
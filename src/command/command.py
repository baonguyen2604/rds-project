# Base command class
class Command():
    name = "BaseCommand"
    response = ""
    def __init__(self, args):
        pass

    def run(self):
        return ""

    @property
    def description(self):
        pass

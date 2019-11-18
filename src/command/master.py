from command import Command

class Master(Command):
    name = "MasterCommand"

    def __init__(self, args):
        super.__init__(Master, args)
        self.options['ip'] = args['ip']
        self.options['port'] = args['port']
        self.options['heartbeat'] = args['heartbeat']
        self.options['peers'] = args['peers']

    @property
    def run(self):
        print("Master run")

        master_address, peers = self._check_peers()

        

    @property
    def description(self):
        print("Master description")

    def _check_peers(self):
        master_address = self.options['ip'] + ":" + self.options['port']
        peers = []

        if self.options['peers'] != '':
            peers = self.options['peers'].split(',')

        has_self = False
        for peer in peers:
            if peer == master_address:
                has_self = True
                break

        if not has_self:
            peers.append(master_address)

        return master_address, peers
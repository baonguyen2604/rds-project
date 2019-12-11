import docker
from .command import Command
from server.master_server import MasterServer

class Master(Command):
    name = "MasterCommand"

    def __init__(self, args=None):
        Command.__init__(self, args)
        self.options = {}
        self.options['ip'] = args.ip
        self.options['port'] = args.port
        self.options['grpc_port'] = args.grpc_port

    def run(self):
        print("Master command run")

        # create docker container to run master
        client = docker.from_env()
        master_container = client.containers.run(image='dfs_master', 
                                                command=['python3', '/root/dfs/create_master.py'])
        
        print(master_container.logs())
        # master_address, peers = self._check_peers()
        # master_server = MasterServer()
        
        

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
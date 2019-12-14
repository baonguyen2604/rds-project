from server.master_server import MasterServer

def master(args):
    master = MasterServer(args)
    master.serve()
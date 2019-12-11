import parser
import argparse
from server.master_server import MasterServer

if __name__ == '__main__':
    master_parser = argparse.ArgumentParser()
    parser.add_master_parse(master_parser)

    args = master_parser.parse_args()

    master = MasterServer(args)
    master.serve()
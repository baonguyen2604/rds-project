import argparse

def main_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')

    master = subparsers.add_parser('master')
    add_master_parse(master)

    upload = subparsers.add_parser('upload')
    add_upload_parse(upload)

    volume = subparsers.add_parser('volume')
    add_volume_parse(volume)

    return parser

def add_master_parse(parser):
    parser.add_argument("-p", "--port", type=int, help="port to talk to master", default=12000)
    parser.add_argument("-ip", help="ip of master", default="localhost")
    parser.add_argument("-gp", "--grpc-port", help="grpc port for master", default='12001')

def add_upload_parse(parser):
    parser.add_argument("-p", "--path", help="path to upload to file system", default='.')
    parser.add_argument("--master", help="master GRPC ip address in format <ip>:<port>", default="localhost:12001")

def add_volume_parse(parser):
    parser.add_argument("-id", type=int, help="id of this volume", default=1)
    parser.add_argument("-p", "--port", type=int, help="port to talk to volume", default=13000)
    parser.add_argument("-ip", help="ip of volume", default="localhost")
    parser.add_argument("-gp", "--grpc-port", help="grpc port for volume", default='13001')
    parser.add_argument("--master", help="master GRPC ip address in format <ip>:<port>", default="localhost:12001")
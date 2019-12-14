import argparse

def main_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')

    master = subparsers.add_parser('master')
    add_master_parse(master)

    upload = subparsers.add_parser('upload')
    add_upload_parse(upload)

    return parser

def add_master_parse(parser):
    parser.add_argument("-p", "--port", type=int, help="port to talk to master", default=12000)
    parser.add_argument("-ip", help="ip of master", default="localhost")
    parser.add_argument("-gp", "--grpc-port", help="grpc port for master", default='12001')

def add_upload_parse(parser):
    parser.add_argument("-p", "--path", help="path to upload to file system", default='.')
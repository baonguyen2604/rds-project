import server.volume_server as vs

def volume(args):
    print("Started volume at %s:%d and GRPC port = %s" %(args.ip, args.port, args.grpc_port))
    vs.serve(args)
import server.volume_server as vs

def volume(volume_id, args):
    print("Started volume at %s:%d and GRPC port = %s" %(args.ip, args.port, args.grpc_port))
    vs.serve(volume_id, args)
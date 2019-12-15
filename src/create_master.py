import server.master_server as ms

def master(args):
    ms.serve(args)
    print("Started master at %s:%d and GRPC port = %s" %(args.ip, args.port, args.grpc_port))

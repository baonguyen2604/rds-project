import zmq
import parser
import pickle
import client_upload

SERVER_PORT = 5000

def Client():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)

    # Connect to AWS Instance
    socket.connect("tcp://34.237.189.42:%s" % SERVER_PORT) 
    clientParser = parser.main_parser()
    args = clientParser.parse_args()
    pArgs = pickle.dumps(args)
    socket.send(pArgs)

    if args.command == "upload":
        client_upload.upload(args, context)

    resp = socket.recv_string()
    print(resp)

# Client Process, uses ZMQ to communicate to Main.py
if __name__ == '__main__':
    Client()

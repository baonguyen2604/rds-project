import zmq
import parser
import pickle

SERVER_PORT = 5000

def Client():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://127.0.0.1:%s" % SERVER_PORT) 
    clientParser = parser.main_parser()
    args = clientParser.parse_args()
    pArgs = pickle.dumps(args)
    socket.send(pArgs)

# Client Process, uses ZMQ to communicate to Main.py
if __name__ == '__main__':
    Client()

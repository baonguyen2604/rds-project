import zmq
import time

UPLOAD_PORT = 5002
CHUNK_SIZE = 1000

def upload(args, context):
    publisher = context.socket(zmq.PUB)
    publisher.bind("tcp://127.0.0.1:5200")
    time.sleep(1)
    file = open(args.path, "rb")
    while True:
        data = file.read(CHUNK_SIZE)
        publisher.send_multipart([args.path.encode(), data])
        if not data:
            break
    publisher.close()

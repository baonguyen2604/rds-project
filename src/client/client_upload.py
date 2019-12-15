import zmq
import time

UPLOAD_PORT = 5002
CHUNK_SIZE = 1000

# Uploads files in chunks to the main server
def upload(args, context):
    publisher = context.socket(zmq.PUB)

    # Send files to main process in chunks
    publisher.bind("tcp://34.237.189.42:%s" % UPLOAD_PORT)
    time.sleep(1)
    file = open(args.path, "rb")
    while True:
        data = file.read(CHUNK_SIZE)
        publisher.send_multipart([args.path.encode(), data])
        if not data:
            break
    publisher.close()

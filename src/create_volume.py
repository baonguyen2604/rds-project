from server.volume_server import VolumeServer

def volume(args):
    volume = VolumeServer(args)
    volume.serve()
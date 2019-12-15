# Distributed File System
A simple implementation of a distributed file system using Python. Supports the following features:
- Stores files across multiple different nodes
- Ability store to large files since files are split into small chunks
- Quick read access to files' metadata

## Requirements installation
`pip3 install -r requirements.txt`

## Code structure
### Project directory
- `src/client`:
    - Code and sample use cases for the client
    - Uses ZMQ REQ-REP to send commands to server
    - Uses ZMQ PUB-SUB to send files to server
    - Supported command:
        - `master -ip <ip> -p <port> -gp <grpc_port> -n <name>`
            - command to spawn master with supplied IP addresses, ports and name
        - `volume -ip <ip> -p <port> -gp <grpc_port> -n <name> --master <ip:port>`
            - similar to `master` command but `volume` commands requires an additional argument to specify the master address
        - `upload -p <file_path> --master <ip:port> -n <name>`:
            - command to upload a single file to a specified master
            - currently does not support directory upload
        - `ls -p <file_path> --n <name>`:
            - list all files in the specified master along with their metadata
    - All commands provide default arguments values, except for upload and ls file path
- `src/command`:
    - Command classes that are created based on user command
    - Command logic:
        - `master`: use `multiprocessing` to spawn a new processing running `create_server.py`, supplying it with the same user arguments
        - `volume`: similar to `master` command, also spawn a new process for a new volume node. However, before spawning the process, asks the master for a unique volume_id
- `src/proto`:
    - Contains `protobuf` and gRPC definitions for communication between main server, master server, and volume server
    - `master.proto`: defines gRPC service for master node
    - `volume.proto`: defines gRPC service for volume node
- `src/server`:
    - Server objects for master and volume
    - `master_server.py`: defines MasterServer() class that implements the gRPC service for master. This class is a gRPC server for the main server to talk to. It is also a gRPC client to communicate to volume
    - `volume_server.py`: defines VolumeServer() class that implements the gRPC service for volume. It is also a gRPC server for master to talk to
- `create_master.py` and `create_server.py`: helper scripts to spawn master and volume. These scripts are needed for Python's `multiprocessing` module to easily start a process
- `main.py`: main server script, uses ZMQ REP socket to receive data from client and runs the appropriate commands

## How to test
1. Start up the DFS with `python3 main.py`
2. Spawn a master with `python3 client.py master` (all other commands will fail if ran before master is spawned)
3. Add arbitrary (more than 1) volume nodes using `python3 client.py volume` (upload will fail if there is no volume node)
4. Upload any file with `python3 client.py upload --path <file_path>`

We have provided a simulation scenario in `client` directory. `test.sh` script does the following: spawn master, add 2 volumes, upload test1.txt, upload test2.txt. The result should be test1.txt is in volume_0 and test2.txt is in volume_1

## References
- ![SeaweedFS](https://github.com/chrislusf/seaweedfs/tree/master/)
- ![gRPC](https://grpc.io/)
- ![ZMQ](https://pyzmq.readthedocs.io/en/latest/api/zmq.html)
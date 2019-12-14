# !/bin/bash

# use protoc to compile the protos file
python3 -m grpc_tools.protoc -I. --python_out=./master_pb --grpc_python_out=./master_pb master.proto
python3 -m grpc_tools.protoc -I. --python_out=./volume_pb --grpc_python_out=./volume_pb volume.proto

# due to a bug in the compiler, we need to replace an import line
sed -i "" "s|import\smaster_pb2|from\s.\simport\smaster_pb2|" ./master_pb/master_pb2_grpc.py
sed -i '' 's|import volume_pb2 as volume__pb2|from . import volume_pb2 as volume__pb2' ./volume_pb/volume_pb2_grpc.py
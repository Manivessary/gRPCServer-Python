# gRPCServer-Python

# first of all install protobuf 

$ pip install protobuf
$ pip install grpcio-tools 

# Generate pb2 files from proto files 
$ python -m grpc_tools.protoc -I./protos --python_out=. --pyi_out=. --grpc_python_out=. ./protos/grpcserver.proto


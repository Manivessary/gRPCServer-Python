from concurrent import futures
import logging

import grpc
import grpcserver_pb2
import grpcserver_pb2_grpc


class Greeter(grpcserver_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return grpcserver_pb2.HelloReply(message="Merhaba , %s!" % request.name)


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpcserver_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()

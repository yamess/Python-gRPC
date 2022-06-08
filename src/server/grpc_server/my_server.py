from concurrent import futures

import grpc

from protos.user_pb2_grpc import add_UserServiceServicer_to_server
from routes.user_routes import UserService


def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port("[::]:50051")
    print("gRPC starting")
    server.start()
    server.wait_for_termination()

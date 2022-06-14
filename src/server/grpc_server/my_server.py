import logging
from concurrent import futures

import grpc

from protos.user_pb2_grpc import add_UserServiceServicer_to_server
from routes.user_routes import UserService

logger = logging.getLogger(__name__)


def server():
    _server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    add_UserServiceServicer_to_server(UserService(), _server)
    _server.add_insecure_port("[::]:50051")
    print("gRPC starting...")
    print("gRPC server started at: localhost:50051")
    _server.start()
    _server.wait_for_termination()

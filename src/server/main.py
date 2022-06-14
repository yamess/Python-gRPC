from configs.env_vars import Base, engine
from grpc_server.my_server import server

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    server()

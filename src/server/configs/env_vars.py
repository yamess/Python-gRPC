from dotenv import find_dotenv, load_dotenv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv(find_dotenv())

# Server
HOST = os.environ["GRPC_HOST"]
PORT = os.environ["GRPC_PORT"]

# Database
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_USER = os.environ["DB_USER"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_NAME = os.environ["DB_NAME"]

# DB_URL = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{DB_URI}/AuthSource=Admin?retryWrites=true&w=majority"
DB_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@127.0.0.1:5432/{DB_NAME}"

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os import environ
from os import getenv
# from os.path import exists
# from dotenv import load_dotenv

# USER = environ.get('POSTGRES_USER') or "myuser"
# PASSWORD = environ.get('POSTGRES_PASSWORD') or "abc"
# DB_NAME = environ.get('POSTGRES_DB') or "mydb"
# HOST = "localhost"
# DB_PORT = "5432"
#
# db_url = f"postgresql://{USER}:{PASSWORD}@{HOST}:{DB_PORT}/{DB_NAME}"
# DOTENV_PATH = '../.env'
#
# if exists(DOTENV_PATH):
#     load_dotenv(DOTENV_PATH)

db_url = environ.get('DATABASE_URL')
engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
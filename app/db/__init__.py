from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv 

load_dotenv()

# Connecting to database with env
# Manages the overall connection to database 
# Only allows for 20 simultaneious connection 
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
# Generates temporary connections for performimg CRUD operations
Session = sessionmaker(bind=engine)
# Class variable that helps map models to real MySQL tables 
Base = declarative_base()
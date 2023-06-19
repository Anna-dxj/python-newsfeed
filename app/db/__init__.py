from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv 
from flask import g

load_dotenv()

# Connecting to database with env
# Manages the overall connection to database 
# Only allows for 20 simultaneious connection 
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
# Generates temporary connections for performimg CRUD operations
Session = sessionmaker(bind=engine)
# Class variable that helps map models to real MySQL tables 
Base = declarative_base()

# Initializes database & creates tables before interaction 
def init_db():
    Base.metadata.create_all(engine)

# When function called returns the connection from the g object
def get_db():
    if 'db' not in g: 
        # Stores db connection in app context
        g.db = Session()
    return g.db
from app.db import Base
# Import classes from sqlalchemy to define table columns and datatypes 
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
import bcrypt

# Creates random salt to hash password against 
salt = bcrypt.gensalt()

# User inherits from Base class
# Delcaring several properties that parent Base class will use to make a table
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)

    @validates('email')
    def validate_email(self, key, email):
        # Emsures that email address contains @
        assert '@' in email

        return email 
    
    @validates('password')
    def validate_password(self, key, password):
        # Emsures that email is longer than 4 characters
        assert len(password) > 4

        # Hashes password with salt from earlier
        return bcrypt.hashpw(password.encode('utf-8'), salt)

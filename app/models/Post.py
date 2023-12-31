from datetime import datetime 
from app.db import Base
from .Vote import Vote
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, select, func
from sqlalchemy.orm import relationship, column_property
class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    post_url = Column(String(100), nullable=False)
    # Declares foreign key 
    user_id = Column (Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    # Performs a SELECT with SQLAlchemy `func.count()` method, to add up votes
    # Does: SELECT COUNT(votes.id) AS vote_count FROM votes WHERE votes.post_id = 1;
    # Query for a post should also return information about the number of votes each post has 
    vote_count = column_property(
    select(func.count(Vote.id)).where(Vote.post_id == id)
    )

    # Establishes link between two models by speficying target model/reference to target class itself 
    user = relationship('User')
    comments = relationship('Comment', cascade='all,delete')
    votes = relationship('Vote', cascade='all,delete')
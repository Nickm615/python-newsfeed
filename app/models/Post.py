from datetime import datetime
from app.db import Base
from .Vote import Vote
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, select, func
from sqlalchemy.orm import relationship, column_property
# sqlalchemy supports Datetime module. We use this to save created_at time in our Post table. We also have created a foreignkey 'user_id' which references our User table, and defined the relationship accordingly.
class Post(Base):
  __tablename__ = 'posts'
  user = relationship('User')
  comments = relationship('Comment', cascade='all,delete')
  votes = relationship('Vote', cascade='all,delete')
  id = Column(Integer, primary_key=True)
  title = Column(String(100), nullable=False)
  post_url = Column(String(100), nullable=False)
  user_id = Column(Integer, ForeignKey('users.id'))
  created_at = Column(DateTime, default=datetime.now)
  updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
#  vote_count is a dynamic property which performs a select where id values match and counts the total number of votes using func.count, method imported from sqlalchemy
  vote_count = column_property(
      select([func.count(Vote.id)]).where(Vote.post_id == id)
  )

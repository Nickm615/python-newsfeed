from datetime import datetime
from app.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
# sqlalchemy supports Datetime module. We use this to save created_at time in our Post table. We also have created a foreignkey 'user_id' which references our User table, and defined the relationship accordingly.
class Post(Base):
  __tablename__ = 'posts'
  user = relationship('User')
  comments = relationship('Comment', cascade='all,delete')
  id = Column(Integer, primary_key=True)
  title = Column(String(100), nullable=False)
  post_url = Column(String(100), nullable=False)
  user_id = Column(Integer, ForeignKey('users.id'))
  created_at = Column(DateTime, default=datetime.now)
  updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

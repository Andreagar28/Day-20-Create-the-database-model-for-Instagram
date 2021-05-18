import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

association_table = Table('association', Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('followers_id', Integer, ForeignKey('followers.id'))

)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String)
    lastname = Column(String)
    password = Column(String) 
    mail = Column(String)
    bio = Column(String, nullable=True)
    followers = relationship("Followers",
        secondary=association_table)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, unique=True, primary_key=True)
    media = Column(String)
    description = Column(String, nullable=True) 
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship(User)

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, unique=True, primary_key=True)
    text = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))
    post_id = Column(Integer, ForeignKey("post.id"))
    user = relationship(User)
    post = relationship(Post)

class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, unique=True, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    follower_by = Column(Integer, ForeignKey("user.id"))
    user = relationship(User)
   

    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
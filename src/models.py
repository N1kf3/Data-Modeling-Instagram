import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    creator = Column(String(250), ForeignKey('user.user_name') ,nullable=False)
    media = Column(String(250), ForeignKey('media.id'))

class Comment(Base):
    __tablename__='comment'
    id = Column(Integer, primary_key=True)
    post = Column(String(250), ForeignKey('post.id'))
    user = Column(String(250), ForeignKey('user.id'))
    content = Column(String(250))

class Story(Base):
    __tablename__ = 'story'
    id = Column(Integer, primary_key=True)
    user = Column(String(250), ForeignKey('user.id'))
    media = Column(String(250), ForeignKey('media.id'))


class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    content = Column(String(250) ,nullable=False)




## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e

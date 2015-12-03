# -*- coding: utf8 -*-


from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, sessionmaker

Base = declarative_base()

class Mots(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    year = Column(Integer)
    directed_by = Column(Integer, ForeignKey('directors.id'))

    director = relation("Director", backref='movies', lazy=False)

    def __init__(self, title=None, year=None):
        self.title = title
        self.year = year

    def __repr__(self):
        return "Movie(%r, %r, %r)" % (self.title, self.year, self.director)

class Documents(Base):
    __tablename__ = 'directors'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return "Director(%r)" % (self.name)

engine = create_engine('dbms://user:pwd@host/dbname')
Base.metadata.create_all(engine)
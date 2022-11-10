import os
import sys
import datetime
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'Usuario'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250) )
    password = Column(String(250), nullable=False)
    subscription = Column(DateTime, default=datetime.datetime.utcnow)

class Planetas(Base):
    __tablename__ = 'Planetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))

class Personajes(Base):
    __tablename__ = 'Personajes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))

class Vehiculos(Base):
    __tablename__ = 'Vehiculos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))

class Favoritos_table(Base):
    __tablename__ = 'Favoritos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('Usuario.id'))
    planeta_id = Column(Integer, ForeignKey('Planetas.id'))
    personajes_id = Column(Integer, ForeignKey('Personajes.id'))
    vehiculos_id = Column(Integer, ForeignKey('Vehiculos.id'))
    person = relationship(Person)
    planetas = relationship(Planetas)
    personajes = relationship(Personajes)
    vehiculos = relationship(Vehiculos)
    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base

render_er(Base, 'diagram.png')
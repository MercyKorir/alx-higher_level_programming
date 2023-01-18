#!/usr/bin/python3
"""contains class definition of a State and an
instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Declaration of class State

    __tablename__(str): name of table to store values
    id (sqlalchemy.Integer): id of state
    name (sqlalchemy.String): name of state
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

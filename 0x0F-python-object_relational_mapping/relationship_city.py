#!/usr/bin/python3
"""contains class definition of a City"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """Declaration of class City

    __tablename__(str): name of table to store values
    id (sqlalchemy.Integer): id of city
    name (sqlalchemy.String): name of city
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    state = relationship("State", back_populates="cities")

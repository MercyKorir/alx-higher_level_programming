#!/usr/bin/python3
"""Doc
"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import mapper, relationship, Session

from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    
    session = Session(engine)
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("{}: {}".format(city.id, city.name))
    session.close()

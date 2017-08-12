#!/usr/bin/python3
"""
lists all State objects from a database
"""
import MySQLdb
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    host = 'localhost'
    port = 3306
    user, passwd, database = argv[1], argv[2], argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(user,
                                                                   passwd,
                                                                   host,
                                                                   port,
                                                                   database))
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))

    session.close()

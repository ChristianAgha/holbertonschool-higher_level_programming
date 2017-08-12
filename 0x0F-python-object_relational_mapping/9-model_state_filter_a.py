#!/usr/bin/python3
"""
lists all State objects that contain the
letter a from the database hbtn_0e_6_usa
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

    states_with_a = session.query(State).order_by(State.id).filter(State.name.
                                                                   like('%a%'))
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    session.close()

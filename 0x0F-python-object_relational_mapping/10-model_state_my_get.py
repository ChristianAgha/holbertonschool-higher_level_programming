#!/usr/bin/python3
"""
prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
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
    passed_state = argv[4].split("'")[0]
    not_found = 1

    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(user,
                                                                   passwd,
                                                                   host,
                                                                   port,
                                                                   database))
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    states = session.query(State).order_by(State.id).all()

    for state in states:
        if state.name == passed_state:
            print("{}".format(state.id))
            not_found = 0
    if (not_found):
        print("Not found")

    session.close()

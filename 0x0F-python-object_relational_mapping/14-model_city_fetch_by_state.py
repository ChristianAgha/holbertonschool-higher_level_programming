#!/usr/bin/python3
"""
prints the first State object from a database
"""
import MySQLdb
from sys import argv
from model_state import State
from model_city import City
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

    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        state = session.query(State).filter(State.id == city.state_id).first()
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()

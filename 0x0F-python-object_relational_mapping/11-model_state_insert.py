#!/usr/bin/python3
"""
 adds the State object "Louisiana" to the database hbtn_0e_6_usa
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

    state_insert = State(name="Louisiana")
    session.add(state_insert)
    session.commit()

    print('{}'.format(state_insert.id))

    session.close()

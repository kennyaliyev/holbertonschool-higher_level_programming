#!/usr/bin/python3
"""Add State 'Louisiana' to hbtn_0e_6_usa."""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, database
        ),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create new State object
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Print the new state's id
    print(new_state.id)

    session.close()

from sqlalchemy.orm import sessionmaker
from ORM.create_db import engine

from select_with_connection import select_connection_1, select_connection_2, select_connection_3, select_connection_4, \
    select_connection_5, select_connection_6, select_connection_7

from select_with_session import select_session_1, select_session_2, select_session_3, select_session_4, \
    select_session_5, select_session_6, select_session_7, select_session_8, select_session_9

Session = sessionmaker(bind=engine)
session = Session()
session_without_autocommit = Session(autocommit=True)

if __name__ == '__main__':
    select_session_1(session)
    # select_connection_1()
    # select_session_2(session)
    # select_connection_2()
    # select_session_3(session)
    # select_connection_3()
    # select_session_4(session)
    # select_connection_4()
    # select_session_5(session)
    # select_connection_5()
    # select_session_6(session)
    # select_connection_6()
    # select_session_7(session, 1950, 2020)
    # select_connection_7(1950, 2020)
    # select_session_8(session)
    # select_sessiyon_9(session_without_autocommit)

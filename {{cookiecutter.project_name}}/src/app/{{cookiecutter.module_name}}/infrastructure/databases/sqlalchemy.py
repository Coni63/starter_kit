from __future__ import annotations

from contextlib import contextmanager

from setup import cfg
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Configure your database connection here
DATABASE_URL = cfg["application"]["database_conn_string"]
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@contextmanager
def provide_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

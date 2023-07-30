from __future__ import annotations

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Approach required for pre-commit, otherwise it raise a mypy error
    https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html#declarative-table-with-mapped-column
    """

    pass


class ItemModel(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)

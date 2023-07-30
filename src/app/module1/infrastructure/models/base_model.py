from __future__ import annotations

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Approach required for pre-commit, otherwise it raise a mypy error
    https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html#declarative-table-with-mapped-column
    """

    pass

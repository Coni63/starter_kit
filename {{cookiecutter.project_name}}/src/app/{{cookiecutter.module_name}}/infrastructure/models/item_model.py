from __future__ import annotations

from app.{{cookiecutter.module_name}}.domain import Item
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from .base_model import Base


class ItemModel(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)

    @staticmethod
    def from_pydantic_object(Item: Item):
        """Intanciate the object from the pydantic object

        :param Item: Item to be persisted.
        :return: the SQLAlchemy object
        """
        return ItemModel(
            id=Item.id,
            title=Item.title,
            description=Item.description,
        )

    def to_pydantic_object(self):
        """Convert a record to a pydantic object.
        This is made because the application should not care about the way it is stored.
        The application wants a pydantic object but we cannot persist it as is

        :return: a pydantic object representing the record
        """
        return Item(
            id=self.id,
            title=self.title,
            description=self.description,
        )

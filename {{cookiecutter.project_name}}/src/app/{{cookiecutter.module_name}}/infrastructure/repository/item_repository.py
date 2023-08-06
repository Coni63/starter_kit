from __future__ import annotations

from app.{{cookiecutter.module_name}}.domain.item import Item
from app.{{cookiecutter.module_name}}.infrastructure.models.item_model import ItemModel
from sqlalchemy.orm import Session


class ItemRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_item_by_id(self, id: int) -> Item | None:
        """Function responsible for acquire from the database (or any other source) the item

        :param id: id of the item
        :return: the item object or None if not found
        """
        record = self._get_by_id(id)

        if record is None:
            return None

        return record.to_pydantic_object()

    def get_all_items(self) -> list[Item]:
        """Function responsible for acquire all the items from the database (or any other source)

        :return: all the items objects stored
        """
        records = self.session.query(ItemModel).all()
        return [record.to_pydantic_object() for record in records]

    def create_item(self, item: Item) -> Item:
        """Function responsible for save a new item to the database (or any other source)

        :param item: item to create
        :return: the item object created
        """
        record = ItemModel.from_pydantic_object(item)
        self.session.add(record)
        self.session.commit()
        return record.to_pydantic_object()

    def delete_item(self, id: int) -> bool:
        """Function responsible for delete an item from the database (or any other source)

        :param item: id of the item
        :return: if the object is deleted
        """
        record = self._get_by_id(id)

        if record is None:
            return False

        self.session.delete(record)
        self.session.commit()
        return True

    def update_item(self, id: int, **kwargs) -> Item:
        """Function responsible for update/patch an item from the database (or any other source)

        :param item: id of the item
        :param kwargs: all attributes to patch
        :return: the update instance
        """
        record = self._get_by_id(id)

        if record is None:
            return None

        for key, value in kwargs.items():
            if hasattr(record, key):
                setattr(record, key, value)

        self.session.commit()
        return record.to_pydantic_object()

    def _get_by_id(self, id: int) -> ItemModel:
        """Private method for getting the ItemModel associated to an id. Used in multiple methods

        :param id: id of the record
        :return: the ItemModel instance
        """
        return self.session.query(ItemModel).filter(ItemModel.id == id).first()

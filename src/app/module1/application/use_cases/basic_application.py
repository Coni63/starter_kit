from __future__ import annotations

from app.module1.domain.item import Item
from app.module1.infrastructure.databases.sqlalchemy import provide_session
from app.module1.infrastructure.repository.item_repository import ItemRepository


def get_all_items():
    with provide_session() as session:
        repository = ItemRepository(session)
        all_items = repository.get_all_items()
    return all_items


def get_item_by_id(item_id: int):
    with provide_session() as session:
        repository = ItemRepository(session)
        item = repository.get_item_by_id(item_id)
    return item or {}


def create_item(item: Item):
    with provide_session() as session:
        repository = ItemRepository(session)
        created_item = repository.create_item(item)
    return created_item


def update_item(id, new_item: Item):
    return


def patch_item():
    return


def delete_item(id: int):
    with provide_session() as session:
        repository = ItemRepository(session)
        worked = repository.delete_item(id)
    return {"worked": worked}

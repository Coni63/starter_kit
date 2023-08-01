from __future__ import annotations

import unittest
from unittest.mock import MagicMock

from app.module1.domain import Item
from app.module1.infrastructure.repository.item_repository import ItemModel
from app.module1.infrastructure.repository.item_repository import ItemRepository


class TestItemRepository(unittest.TestCase):
    def setUp(self):
        # Create a mock sqlalchemy session for testing
        self.mock_session = MagicMock()

        # Create an instance of ItemManager with the mock session
        self.item_repository = ItemRepository(session=self.mock_session)

    def test_get_item_by_id_found(self):
        # Create a mock ItemModel object with a specific ID
        mock_item = ItemModel(id=1, title="Item 1", description="Item 1 description")

        # Configure the mock session to return the mock item when queried with ID 1
        self.mock_session.query.return_value.filter.return_value.first.return_value = mock_item

        # Call the method under test with the ID of the item we expect to find (ID 1)
        result = self.item_repository.get_item_by_id(1)

        # Assert that the result is an instance of Item (assuming Item is your model class)
        # You can modify this check based on your actual implementation
        self.assertIsInstance(result, Item)

    def test_get_item_by_id_not_found(self):
        # Configure the mock session to return None when queried with any ID
        self.mock_session.query.return_value.filter.return_value.first.return_value = None

        # Call the method under test with an ID that does not exist in the mock session
        result = self.item_repository.get_item_by_id(999)

        # Assert that the result is None since the item was not found
        self.assertIsNone(result)

    def test_get_all_items(self):
        # Create a list of mock ItemModel objects
        mock_items = [
            ItemModel(id=1, title="Item 1", description="Item 1 description"),
            ItemModel(id=2, title="Item 2", description="Item 2 description"),
        ]

        # Configure the mock session to return the mock items when queried
        self.mock_session.query.return_value.all.return_value = mock_items

        # Call the method under test
        result = self.item_repository.get_all_items()

        # Assert that the result is a list of Item objects
        self.assertIsInstance(result, list)

        # Assert that the number of items in the result matches the number of mock items
        self.assertEqual(len(result), len(mock_items))

        # Assert that each item in the result is of type Item (assuming Item is your model class)
        # You can modify this check based on your actual implementation
        for item in result:
            self.assertIsInstance(item, Item)

    def test_create_item(self):
        # Create a mock Item object
        mock_item = Item(id=None, title="Item 1", description="Item 1 description")
        mock_return = ItemModel(id=1, title="Item 1", description="Item 1 description")

        # Configure the mock session to return the ItemModel record when queried after addition
        self.mock_session.query.return_value.filter.return_value.first.return_value = mock_return
        self.mock_session.add.return_value = None
        self.mock_session.commit.return_value = None

        # Call the method under test with the mock item
        result = self.item_repository.create_item(mock_item)

        # Assert that the result is an instance of Item (assuming Item is your model class)
        # You can modify this check based on your actual implementation
        self.assertIsInstance(result, Item)
        self.assertEqual(result.title, mock_item.title)
        self.assertEqual(result.description, mock_item.description)

        # unfortunately we cannot check that the id is backpopulated to the Item from the ItemModel
        # self.assertIsNotNone(result.id)

    def test_delete_id_found(self):
        # Create a mock ItemModel object with a specific ID
        mock_item = ItemModel(id=1, title="Item 1", description="Item description")

        # Configure the mock session to return the mock item when queried with ID 1
        self.mock_session.query.return_value.filter.return_value.first.return_value = mock_item

        # Configure the mock session's delete and commit methods
        self.mock_session.delete.return_value = None
        self.mock_session.commit.return_value = None

        # Call the method under test with the ID of the item we want to delete (ID 1)
        result = self.item_repository.delete_item(1)

        # Assert that the result is True since the item was found and deleted successfully
        self.assertTrue(result)

    def test_delete_id_not_found(self):
        # Configure the mock session to return None when queried with any ID
        self.mock_session.query.return_value.filter.return_value.first.return_value = None

        # Call the method under test with an ID that does not exist in the mock session (ID 999)
        result = self.item_repository.delete_item(999)

        # Assert that the result is False since the item was not found and deletion was unsuccessful
        self.assertFalse(result)

    def test_update_item_with_keys(self):
        # Create a mock ItemModel object with a specific ID
        mock_item = ItemModel(id=1, title="Item 1", description="Description 1")

        # Configure the mock session to return the mock item when queried with ID 1
        self.mock_session.query.return_value.filter.return_value.first.return_value = mock_item

        # Configure the mock session's commit method
        self.mock_session.commit.return_value = None

        # Call the method under test with the ID of the item we want to update (ID 1) and the attributes to patch
        result = self.item_repository.update_item(1, title="Updated Item")

        # Assert that the result is an instance of Item (assuming Item is your model class)
        self.assertIsInstance(result, Item)

        # Assert that the item's attributes were properly updated
        self.assertEqual(result.id, 1)
        self.assertEqual(result.title, "Updated Item")
        self.assertEqual(result.description, "Description 1")

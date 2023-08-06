from __future__ import annotations

import unittest

from app.{{cookiecutter.module_name}}.domain import Item


class TestItemRepository(unittest.TestCase):
    def test_valid_input(self):
        item = Item(title="name 1", description="Description-1")

        self.assertEqual(item.title, "name 1")
        self.assertEqual(item.description, "Description-1")

    def test_corrected_input(self):
        item = Item(title="name 1", description="kožušček 北亰 François")

        self.assertEqual(item.title, "name 1")
        self.assertEqual(item.description, "ko_u__ek __ Fran_ois")

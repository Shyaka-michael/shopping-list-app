"""
module for testing item class
"""

import unittest
from ..shopping_classes.shopping_item import Item


class TestShoppingItem(unittest.TestCase):
    """
    main class to test item class name and quantity
    """

    def setUp(self):
        self.item_one = Item("soap", 3)

    def test_item(self):
        """
            methods for testing item class name and quantity
        """
        print(self.item_one)
        self.assertEqual(self.item_one.name, "soap", msg='item not found')
        self.assertEqual(self.item_one.quantity, 3, msg='quantity not found')

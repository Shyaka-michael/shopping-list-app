import unittest
from ..shopping_classes.shopping_item import Item


class Test_shopping_item(unittest.TestCase):

    def setUp(self):
        self.item_one = Item("soap", 3)

    def test_item(self):
        print(self.item_one)
        self.assertEqual(self.item_one.name, "soap", msg='item not found')
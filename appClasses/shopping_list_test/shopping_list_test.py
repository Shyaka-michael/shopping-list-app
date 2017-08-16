"""
module for testing shopping list
"""
import unittest
from ..shopping_classes.shopping_list import ShoppingList

class TestShoppingList(unittest.TestCase):
    """
    class for the test cases
    """
    def setUp(self):
        self.item_list_one = ShoppingList('groceries')

    def test_list_name(self):
        """
        function tests shopping list name
        """
        #print(self.item_one)
        self.assertEqual(self.item_list_one.list_name, "groceries", msg='item not found')

    def test_add_item_to_list(self):
        """
        function tests for adding am item to the shopping list
        """
        self.item_list_one.add_item('soap', 3)
        self.assertEqual(len(self.item_list_one.list_of_items), 1, msg="item not added")

    def test_edit_item(self):
        """
        function tests for editing a shopping list item
        """
        self.item_list_one.add_item('soap', 3)
        item_edited = self.item_list_one.edit_item('soap', 'vim', 10)
        self.assertEqual(item_edited.name, 'vim', msg='did not edit item')

    def test_delete_item(self):
        """
        function tests for deleting a shopping list item
        """
        self.item_list_one.add_item('soap', 3)
        self.item_list_one.delete_item('soap')
        self.assertEqual(len(self.item_list_one.list_of_items), 0, msg="item not added")

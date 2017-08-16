import unittest
from ..shopping_classes.shopping_list import Shopping_List


class Test_shopping_list(unittest.TestCase):

    def setUp(self):
        self.item_list_one = Shopping_List('groceries')

    def test_list_name(self):
        #print(self.item_one)
        self.assertEqual(self.item_list_one.list_name, "groceries", msg='item not found')

    def test_add_item_to_list(self):
        self.item_list_one.add_item('soap', 3)
        self.assertEqual(len(self.item_list_one.list_of_items), 1, msg="item not added")

    def test_edit_item(self):
        self.item_list_one.add_item('soap', 3)
        item_edited = self.item_list_one.edit_item('soap', 'vim', 10)
        self.assertEqual(item_edited.name, 'vim', msg='did not edit item')

    def test_delete_item(self):
        self.item_list_one.add_item('soap', 3)
        self.item_list_one.delete_item('soap')
        self.assertEqual(len(self.item_list_one.list_of_items), 0, msg="item not added")

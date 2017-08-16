import unittest
from ..shopping_classes.user import User

class TestUserTests(unittest.TestCase):
    def setUp(self):
        self.test_user_case = User('john', 'doe', 'doe', 'doe')

    def test_user_atributes(self):
        self.assertEqual(self.test_user_case.first_name, 'john', msg="insert name")
        self.assertEqual(self.test_user_case.last_name, 'doe', msg="insert name")
        self.assertEqual(self.test_user_case.email, 'doe', msg="insert name")
        self.assertEqual(self.test_user_case.password, 'doe', msg="insert name")

    def test_create_shoppinglist(self):
        self.test_user_case.create_shoppingList("groceries")
        self.assertEqual(len(self.test_user_case.list_of_shopping_list), 1, msg='did not add to list')

    def test_edit_shoppinglist(self):
        self.test_user_case.create_shoppingList("groceries")
        list_edited = self.test_user_case.edit_shoppingList('groceries', 'clothing')
        self.assertEqual(list_edited.list_name, 'clothing', msg='did not add to list')

    def test_delete_shoppinglist(self):
        self.test_user_case.create_shoppingList("groceries")
        self.test_user_case.delete_shoppinglisst('groceries')
        self.assertEqual(len(self.test_user_case.list_of_shopping_list), 0, msg="item not added")




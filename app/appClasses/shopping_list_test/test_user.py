"""
module to test User class
"""
import unittest
from ..shopping_classes.user import User

class TestUserTests(unittest.TestCase):
    """
    main class for user test cases
    """
    def setUp(self):
        self.test_user_case = User('john', 'doe', 'doe', 'doe')

    def test_user_attributes(self):
        """
        function to test user attributes
        """
        self.assertEqual(self.test_user_case.first_name, 'john', msg="insert first_name")
        self.assertEqual(self.test_user_case.last_name, 'doe', msg="insert last_name")
        self.assertEqual(self.test_user_case.email, 'email', msg="insert email")
        self.assertEqual(self.test_user_case.password, 'password', msg="insert password")

    def test_create_shoppinglist(self):
        """
        function to test if a shopping list is created
        """
        self.test_user_case.create_shopping_list("groceries")
        self.assertEqual(len(self.test_user_case.list_of_shopping_list),
                         1, msg='did not add to list')

    def test_edit_shopping_list(self):
        """
        function to test if a shopping list can be edited
        """
        self.test_user_case.create_shopping_list("groceries")
        list_edited = self.test_user_case.edit_shopping_list('groceries', 'clothing')
        self.assertEqual(list_edited.list_name, 'clothing', msg='did not add to list')

    def test_delete_shopping_list(self):
        """
        function to test if a shopping a list can be deleted
        """
        self.test_user_case.create_shopping_list("groceries")
        self.test_user_case.delete_shopping_list('groceries')
        self.assertEqual(len(self.test_user_case.list_of_shopping_list), 0, msg="item not added")

import unittest
from ..shopping_classes.shopping_app import ShoppingApp

class TestShoppingAppCases(unittest.TestCase):
    def setUp(self):
        self.test_app = ShoppingApp()

    def test_create_user(self):
        self.test_app.create_user('john', 'doe', 'email', 'password')
        self.assertEqual(len(self.test_app.list_of_users), 1, msg='user not added')

    def test_edit_user(self):
        self.test_app.create_user('john', 'doe', 'email', 'password')
        user_edited = self.test_app.edit_user('john', 'mary', 'doe', 'email', 'password')
        self.assertEqual(user_edited.first_name, 'mary', msg="not edited ")

    def test_delete_user(self):
        self.test_app.create_user('john', 'doe', 'email', 'password')
        self.test_app.delete_user('email')
        self.assertEqual(len(self.test_app.list_of_users), 0, msg='user not deleted')

    def test_login_user(self):
        self.test_app.create_user('john', 'doe', 'email', 'password')
        self.test_app.login_user("email", "password")
        self.assertIsNotNone(self.test_app.current_user, msg='user not logged in')

    def test_log_out(self):
        self.test_app.create_user('john', 'doe', 'email', 'password')
        self.test_app.log_out()
        self.assertIsNone(self.test_app.current_user, msg="not logged out")

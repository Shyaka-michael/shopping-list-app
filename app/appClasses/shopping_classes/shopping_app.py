"""
module for shopping App class
"""
from..shopping_classes.user import User
class ShoppingApp():
    """
    shopping app class in which one can create a user,edit,login,logout
    """
    def __init__(self):
        """
        function for setting current_user and list_of_users
        """
        self.current_user = None
        self.list_of_users = []
        self.current_shoppinglist = None

    def create_user(self, first_name, last_name, email, password):
        """
        function to create user
        """
        user_created = User(first_name, last_name, email, password)
        self.list_of_users.append(user_created)

    def edit_user(self, first_name, edited_first_name,
                  edited_last_name, edited_email, edited_password):
        """
        function to edit user
        """
        for obj in self.list_of_users:
            if obj.first_name == first_name:
                obj.first_name = edited_first_name
                obj.last_name = edited_last_name
                obj.email = edited_email
                obj.password = edited_password
                return obj

    def delete_user(self, email):
        """
        function to delete user
        """
        for obj in self.list_of_users:
            if obj.email == email:
                self.list_of_users.remove(obj)

    def login_user(self, email, password):
        """
        function to log in
        """
        for obj in self.list_of_users:
            if obj.email == email and obj.password == password:
                self.current_user = obj

    def log_out(self):
        """
        function to log out
        """
        self.current_user = None

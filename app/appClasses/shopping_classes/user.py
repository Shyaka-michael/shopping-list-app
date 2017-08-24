"""
module for user class
"""
from ..shopping_classes.shopping_list import ShoppingList

class User:
    """
    user class with the user methods
    """
    def __init__(self, first_name, last_name, email, password):
        """
        user attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.list_of_shopping_list = []

    def create_shopping_list(self, list_name, id):
        """
        function to create shopping list
        """
        id = len(self.list_of_shopping_list)
        list_item = ShoppingList(list_name,id)
        #print(self.list_of_shopping_list)
        return self.list_of_shopping_list.append(list_item)



    def edit_shopping_list(self, old_name, new_name):
        """
        function to edit a shopping list
        """
        for obj in self.list_of_shopping_list:
            if old_name == obj.list_name:
                obj.list_name = new_name
                return obj

    def delete_shopping_list(self, list_name):
        """
        function to delete a shopping list
        """
        for obj in self.list_of_shopping_list:
            if list_name == obj.list_name:
                self.list_of_shopping_list.remove(obj)

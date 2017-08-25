"""
module for shopping list
"""
from ..shopping_classes.shopping_item import Item

class ShoppingList():
    """
    class shopping list
    """

    def __init__(self, list_name):
        """
        set atributes
        """
        self.list_name = list_name
        self.list_of_items = []
        #self.id =id

    def add_item(self, name, quantity):
        """
        function to add a shopping list item
        """
        new_item = Item(name, quantity)
        self.list_of_items.append(new_item)

    def edit_item(self, item_name, new_name, new_qunatity):
        """
        function to edit shopping list item
        """
        for obj in self.list_of_items:
            if item_name == obj.name:
                obj.name = new_name
                obj.quantity = new_qunatity
                return obj

    def delete_item(self, name):
        """
        function to delete shopping list item
        """
        for obj in self.list_of_items:
            if name == obj.name:
                self.list_of_items.remove(obj)

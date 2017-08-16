from ..shopping_classes.shopping_item import Item

class Shopping_List:
    def __init__(self, list_name):
        self.list_name = list_name
        self.list_of_items = []

    def add_item(self, name, quantity):
        new_item = Item(name, quantity)
        self.list_of_items.append(new_item)

    def edit_item(self, item_name, new_name, new_qunatity):
        for obj in self.list_of_items:
            if item_name == obj.name:
                obj.name = new_name
                obj.quantity = new_qunatity
                return obj

    def delete_item(self, name):
        for obj in self.list_of_items:
            if name == obj.name:
                self.list_of_items.remove(obj)



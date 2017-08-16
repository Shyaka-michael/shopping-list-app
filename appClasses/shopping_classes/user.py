from..shopping_classes.shopping_list import Shopping_List
class User():
    def __init__(self,first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.list_of_shopping_list = []

    def create_shoppingList(self, list_name):
        list_item = Shopping_List(list_name)
        self.list_of_shopping_list.append(list_item)

    def edit_shoppingList(self, old_name, new_name):
        for obj in self.list_of_shopping_list:
            if old_name == obj.list_name:
                obj.list_name = new_name
                return obj

    def delete_shoppinglisst(self, list_name):
        for obj in self.list_of_shopping_list:
            if list_name == obj.list_name:
                self.list_of_shopping_list.remove(obj)


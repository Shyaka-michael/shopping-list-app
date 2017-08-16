from..shopping_classes.user import User

class ShoppingApp():
    def __init__(self):
        self.current_user = None
        self.list_of_users = []

    def create_user(self,first_name, last_name, email, password):
        user_created = User(first_name, last_name, email, password)
        self.list_of_users.append(user_created)

    def edit_user(self,first_name, edited_first_name, edited_last_name, edited_email, edited_password ):
        for obj in self.list_of_users:
           if obj.first_name == first_name:
               obj.first_name = edited_first_name
               obj.last_name = edited_last_name
               obj.email = edited_email
               obj.password = edited_password
               return obj

    def delete_user(self, email):
        for obj in self.list_of_users:
            if obj.email == email:
                self.list_of_users.remove(obj)

    def login_user(self, email, password):
        for obj in self.list_of_users:
            if obj.email == email and obj.password == password:
                self.current_user = obj

    def log_out(self):
        self.current_user = None

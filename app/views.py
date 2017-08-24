from flask import render_template, request,redirect,url_for
#from app import app
from app.appClasses.shopping_classes.shopping_app import ShoppingApp
from app.appClasses.shopping_classes.user import User
from app.appClasses.shopping_classes.shopping_list import ShoppingList

from flask import Flask

app = Flask(__name__)

ShoppingApp = ShoppingApp()
user = User('first_name', 'last_name', 'email', 'password')
listitem = ShoppingList("list_name","id")
current_shopoinglist = None

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        return render_template('login.html', title='Home')
    if request.method == 'POST':
        user_email = request.form['email']
        user_password = request.form['password']
        ShoppingApp.login_user(user_email, user_password)
        if ShoppingApp.current_user:
            return render_template('shoppinglist.html')
        return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'GET':
        return render_template('register.html', title='sing up')
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        password = request.form['password']
        ShoppingApp.create_user(fname, lname, email, password)
        return render_template('login.html', title='Home')


@app.route('/shoppinglist', methods=['GET', "POST"])
def shopping_list():
    print("users currently ")
    print(ShoppingApp.current_user)
    if ShoppingApp.current_user:
        if request.method == "GET":
            shoppinglist_data = ShoppingApp.current_user.list_of_shopping_list
            return render_template('shoppinglist.html', data=shoppinglist_data)
        if request.method == "POST":
            name = request.form["name"]
            user.create_shopping_list(name,"id")
            list_created = user.list_of_shopping_list
            #list_created = User.create_shopping_list(name)
            data = list_created
            print(data)
            return render_template('shoppinglist.html',data=list_created)
    return render_template('login.html')


@app.route('/shoppingitem/<int:shoppingId>', methods=['GET','POST'])
def shopping_item(shoppingId):

    if ShoppingApp.current_user:
        if request.method == "GET":
            #ShoppingApp.current_shoppinglist = ShoppingApp.current_user.list_of_shopping_list[shoppingId]
            #itemdata = ShoppingApp.current_shoppinglist.list_of_items
            return render_template('shoppingitem.html', id=shoppingId)
        elif request.method == "POST":
            name = request.form["name"]
            quantity = request.form["quantity"]
            listitem.add_item(name,quantity)
            itemdata = listitem.list_of_items
            return redirect(url_for(shopping_item(shoppingId), itemdata=itemdata))
    return render_template('login.html')


if __name__ == "__main__":
    app.run()
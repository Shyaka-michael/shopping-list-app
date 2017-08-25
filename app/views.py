from flask import render_template, request,redirect,url_for
from app import app
from app.appClasses.shopping_classes.shopping_app import ShoppingApp
from app.appClasses.shopping_classes.user import User
from app.appClasses.shopping_classes.shopping_list import ShoppingList


ShoppingApp = ShoppingApp()
#user = User('first_name', 'last_name', 'email', 'password')
#listitem = ShoppingList("list_name")
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


@app.route('/shoppinglist', methods=['GET','POST'])
def shoppinglist():

    if ShoppingApp.current_user:
        if request.method == "GET":
            data = ShoppingApp.current_user.list_of_shopping_list
            return render_template('shoppinglist.html',data =data)
        if request.method == 'POST':
            name = request.form['name']
            ShoppingApp.current_user.create_shopping_list(name)
            data = ShoppingApp.current_user.list_of_shopping_list
            #return render_template('shoppinglearn.html')
            return render_template('shoppinglist.html', data=data)
            #return render_template('shoppinglist.html', data=data)


@app.route('/viewshopping/<int:shoppingId>', methods=['GET','POST'])
def viewshopping(shoppingId):

    if ShoppingApp.current_user:
        current_shopoinglist = shoppingId
        if request.method == "GET":
            data = ShoppingApp.current_user.list_of_shopping_list[shoppingId].list_of_items
            return render_template('shoppingitem.html', data=data)
        elif request.method == 'POST':
            pass

@app.route('/deleteshopping/<int:shoppingId>', methods=['GET', 'POST'])
def deleteshopping(shoppingId):
    if ShoppingApp.current_user:
        if request.method == 'GET':
            shooping_name = ShoppingApp.current_user.list_of_shopping_list[shoppingId].list_name
            ShoppingApp.current_user.delete_shopping_list(shooping_name)
            return redirect(url_for('shoppinglist'))



if __name__ == "__main__":
    app.run()
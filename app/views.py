from flask import render_template, request
from app import app
from  .appClasses.shopping_classes.shopping_app import ShoppingApp


ShoppingApp = ShoppingApp()

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('login.html', title='Home')
    if request.method == 'POST':
        user_email = request.form['email']
        user_password = request.form['password']
        ShoppingApp.login_user(user_email, user_password)
        return render_template('shoppinglist.html')


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
    if request.method =="GET":
        shoppinglist_data = ShoppingApp.current_user.list_of_shopping_list
        return render_template('shoppinglist.html', data=shoppinglist_data)
    if request.method == "POST":
        name = request.form["name"]
        ShoppingApp.current_user.create_shopping_list(name)
        shoppinglist_data = ShoppingApp.current_user.list_of_shopping_list
        return render_template('shoppinglist.html', data=shoppinglist_data)

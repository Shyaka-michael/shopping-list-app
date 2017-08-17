from flask import render_template
from app import app

@app.route('/')
@app.route('/login')
def index():
    user = {'nickname': 'Miguel'}
    return render_template('login.html', title='Home', user=user)


@app.route('/register')
def sign_up():
    #user = {'nickname': 'Miguel'}
    return render_template('register.html', title='sing up')

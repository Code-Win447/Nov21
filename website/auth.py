from flask import Blueprint, render_template, request
from flask.helpers import flash

auth =  Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<p> logout </p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        if len(username) < 2:
            flash("Username must be more than 2 Letters", category='error')
        elif len(password) < 7:
            flash("password must be more than 7 letters", category='error')
        else:
            flash("Account Created!", category='success')
            #add user to the database
    return render_template("sign-up.html")
import os
from flask import Flask, render_template, session, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bc = Bcrypt(app)

from models import Users

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    session.clear()

    if request.method == 'POST':

        if not request.form.get('username'):
            return 'Must provide a username.'

        elif not request.form.get('password'):
            return 'Must provide a password.'

        rows = db.execute("SELECT * FROM users WHERE username = :user", {"user": request.form.get('username')}).fetchall()

        if not rows or not bc.check_password_hash(request.form.get('password'), rows[0]['password']):
            flash('Invalid username and/or password.')
            return redirect(url_for('login'))

        session['user_id'] = rows[0]['username']

        flash('Logged In!')
        return redirect(url_for('home'))

    else:
        return render_template('login.html')

@app.route("/logout")
def logout():
    """Log user out."""

    # forget any user_id
    session.clear()

    # redirect user to login form
    return redirect(url_for("login"))

@app.route('/register', methods=['POST'])
def register():
    error = None

    session.clear()

    if request.method == 'POST':

        if not request.form.get('username'):
            flash('Must provide a username.')
            return redirect(url_for('register'))

        if not request.form.get('password'):
            error = 'Must provide a password.'
            return redirect(url_for('register'))

        elif not request.form.get('password2') or request.form.get('password') != request.form.get('password2'):
            error = "Passwords don't match"
            return redirect(url_for('register'))

        rows = db.execute("SELECT * FROM users WHERE username = :user", {"user": request.form.get('username')}).first()

        if rows:
            error = 'Username in use. Please choose another.'
            return redirect(url_for('register'))

        db.execute("INSERT INTO users (username, password) VALUES(:username, :password)", {"username": request.form.get("username"), "password": bc.generate_password_hash(request.form.get('password'))}).decode('utf-8')

        newRows = db.execute("SELECT * FROM users WHERE username = :username", {"username": request.form.get('username')}).fetchall()

        session['user_id'] = newRows[0]['username']

        db.commit()
        flash('Registered')
        return redirect(url_for("home"))

if __name__ == "__main__":
    app.run()
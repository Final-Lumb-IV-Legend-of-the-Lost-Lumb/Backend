import os
from flask import Flask, render_template, session, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp

Session = sessionmaker()
engine = create_engine(os.environ['DATABASE_URL'])
Session.configure(bind=engine)
db_session = Session()

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
bc = Bcrypt(app)
db = SQLAlchemy(app)

from models import Users

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/protected')
@jwt_required()
def protected():
    flash('Yay you are authenticated!')
    return

@app.route('/login', methods=['GET', 'POST'])
def login():

    session.clear()

    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')

        if not request.form.get('username'):
            return 'Must provide a username.'

        elif not request.form.get('password'):
            return 'Must provide a password.'

        registered_user = Users.query.filter_by(username=username).first()

        # Possibly use .decode('utf-8')
        if not registered_user or not bc.check_password_hash( registered_user.password, password):
            flash('Invalid username and/or password.')
            return redirect(url_for('login'))

        @jwt.authentication_handler
        def authenticate(username, password):
            user = Users.query.filter(Users.username == username).scalar()
            if bc.check_password_hash(user.password, password):
                return user
                
        @jwt.identity_handler
        def identify(payload):
            return Users.query.filter(Users.id == payload['identity']).scalar()

        token = JWT(app, authenticate, identify)
        session['user_id'] = registered_user.username

        flash('Logged In!')
        print(token)
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

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None

    session.clear()

    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')

        if not request.form.get('username'):
            flash('Must provide a username.')
            return redirect(url_for('register'))

        if not request.form.get('password'):
            error = 'Must provide a password.'
            return redirect(url_for('register'))

        elif not request.form.get('password2') or request.form.get('password') != request.form.get('password2'):
            error = "Passwords don't match"
            return redirect(url_for('register'))

        user = Users(username, bc.generate_password_hash(password).decode('utf-8'))
        db_session.add(user)
        db_session.commit()

        session['user_id'] = username

        flash('Registered')
        return redirect(url_for("home"))
    
    else:
        return render_template('register.html')

if __name__ == "__main__":
    app.run()
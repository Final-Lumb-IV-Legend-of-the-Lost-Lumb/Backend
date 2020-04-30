import os
from flask import Flask, render_template, session, redirect, url_for, flash, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt, JWTManager, set_access_cookies, unset_jwt_cookies, set_refresh_cookies)

Session = sessionmaker()
engine = create_engine(os.environ['DATABASE_URL'])
Session.configure(bind=engine)
db_session = Session()

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_SECURE'] = True
app.config['JWT_COOKIE_CSRF_PROTECT'] = True
app.config['JWT_ACCESS_COOKIE_PATH'] = '/api/'
app.config['JWT_REFRESH_COOKIE_PATH'] = '/token/refresh'
bc = Bcrypt(app)
db = SQLAlchemy(app)
app.config['JWT_SECRET_KEY'] = 'is-it-secret-is-it-safe'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
jwt = JWTManager(app)

from models import Users, RevokedTokenModel

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return RevokedTokenModel.is_jti_blacklisted(jti)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/api/lobby', methods=['GET'])
@jwt_required
def lobby():
    username = get_jwt_identity()
    return render_template('lobby.html', username = username)

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

        try:
            access_token = create_access_token(identity=username)
            refresh_token = create_refresh_token(identity=username)

            session['user_id'] = registered_user.username
            resp = make_response(redirect(url_for('lobby')))
            set_access_cookies(resp, access_token)
            set_refresh_cookies(resp, refresh_token)
            return resp
        except:
            return jsonify({'message': 'Something went wrong'}), 500

    else:
        return render_template('login.html')

@app.route("/logout", methods=['POST'])
@jwt_required
def logout():
    """Log user out."""

    # forget any user_id
    session.clear()
    resp = jsonify({'logout': True})

    jti = get_raw_jwt()['jti']
    try:
        unset_jwt_cookies(resp)
        revoked_token = RevokedTokenModel(jti = jti)
        revoked_token.add()
        return jsonify({'message': 'Access token has been revoked.'})
    except:
        return jsonify({'message': 'Something went wrong.'}), 500

@app.route('/token/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)
    resp = jsonify({'refresh': True})
    set_access_cookies(resp, access_token)
    return resp, 200

@app.route("/logout/refresh")
@jwt_refresh_token_required
def logout_refresh():
    jti = get_raw_jwt()['jti']
    try:
        revoked_token = RevokedTokenModel(jti = jti)
        revoked_token.add()
        return jsonify({'message': 'Refresh token has been revoked.'})
    except:
        return jsonify({'message': 'Something went wrong.'}), 500

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

        try:
            access_token = create_access_token(identity=username)
            refresh_token = create_refresh_token(identity=username)

            session['user_id'] = username
            resp = make_response(redirect(url_for('lobby')))
            set_access_cookies(resp, access_token)
            set_refresh_cookies(resp, refresh_token)

            return resp
        except:
            return jsonify({'message': 'Something went wrong'}), 500
    
    else:
        return render_template('register.html')

if __name__ == "__main__":
    app.run()
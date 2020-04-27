import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Users

@app.route('/')
def home():
    return render_template('home.html')

# @app.route('/register')
# def register():


if __name__ == "__main__":
    app.run(debug=True)
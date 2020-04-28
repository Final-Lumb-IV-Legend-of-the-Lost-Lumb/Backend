from app import db_session
from sqlalchemy.dialects.postgresql import JSON



class Users(db.Model):
    __tablename__ = 'users'

    id = db_session.Column(db_session.Integer, primary_key=True)
    username = db_session.Column(db_session.String())
    password = db_session.Column(db_session.String())

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def __str__(self):
        return "User(id='%s')" % self.id
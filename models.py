from app import db
from sqlalchemy.dialects.postgresql import JSON

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(), nullable = False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def __str__(self):
        return "User(id='%s')" % self.id

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username = username).first()

class RevokedTokenModel(db.Model):
    __tablename__ = 'revoked_tokens'
    id = db.Column(db.Integer, primary_key = True)
    jti = db.Column(db.String(120))
    
    def add(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def is_jti_blacklisted(cls, jti):
        query = cls.query.filter_by(jti = jti).first()
        return bool(query)
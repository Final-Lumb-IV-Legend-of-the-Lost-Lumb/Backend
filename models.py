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


class Players(db.Model):
    __tablename__ = 'players'
    player_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.string(120), db.ForeignKey('users.username'), unique = True,
        nullable=False)
    inventory = db.relationship('PlayerInventory', backref='players', lazy=True)
    money = db.Column(db.Integer(), nullable = False)


    def __init__(self, money, inventory={}):
        self.money = money

class Items(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key = True)
    item_name = db.Column(db.String(120), nullable=False)
    buying_value = db.Column(db.Integer(), nullable = False)
    selling_value = db.Column(db.Integer(), nullable = False)
    attribute = db.Column(db.String(120), nullable=False)
    item_type = db.Column(db.String(120), nullable=False)

    def __init__(self, item_name, buying_value, selling_value, attribute, item_type ):
        self.item_name = item_name
        self.buying_value = buying_value
        self.selling_value = selling_value
        self.attribute = attribute
        self.item_type = item_type

class PlayerInventory(db.Model):
    __tablename__ = 'player_inventory'
    item_id = db.Column(db.string(120), db.ForeignKey('items.id'), unique = True,
        nullable=False)
    username = db.Column(db.string(120), db.ForeignKey('users.username'), unique = True,
        nullable=False)
    item_name = db.Column(db.string(120), db.ForeignKey('items.item_name'), unique = True,
        nullable=False)
    quantity = db.Column(db.Integer(), nullable = False)
    

    def __init__(self, quantity):
        self.quantity = quantity

class RoomInventory(db.Model):
    __tablename__ = 'room_inventory'
    item_id = db.Column(db.Integer, db.ForeignKey('items.item.id'),
        nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.room.id'),
        nullable=False)
    item_name = db.Column(db.string(120), db.ForeignKey('items.item_name'), unique = True,
        nullable=False)
             
      

class Rooms(db.Model):
    __tablename__ = 'rooms'

    id = db.Column(db.Integer, primary_key = True)
    room_name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    n_to =  db.Column(db.Integer(), nullable = False)
    e_to =  db.Column(db.Integer(), nullable = False)
    s_to =  db.Column(db.Integer(), nullable = False)
    w_to =  db.Column(db.Integer(), nullable = False)
    items =  db.Column(db.PickleType(mutable=True), nullable = False)



    def __init__(self, room_name, description, n_to=None, e_to=None, s_to=None, w_to=None, items={}):
        self.room_name = room_name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = items



    
     











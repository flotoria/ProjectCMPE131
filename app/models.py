from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import login
from flask_login import UserMixin

class User(db.Model, UserMixin): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(32), nullable=False)
    
    # Generate a password hash then set it to its password field
    def set_password(self, password):
        self.password = generate_password_hash(password)

    # Checks whether the plaintext password matches the hashed one in the SQL database
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    # Returns a string representation of the user when queried
    def __repr__(self):
        return f'<user {self.id} : {self.username}>'
    
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(256), nullable=False) 
    body = db.Column(db.String(1000))
    timestamp = db.Column(db.DateTime, default=datetime.now())

    sending_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    receiving_user = db.Column(db.Integer, db.ForeignKey('user.id'))


    def __repr__(self):
        return f'{self.id} : {self.subject}'

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
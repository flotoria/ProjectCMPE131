from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import login
from flask_login import UserMixin

class User(db.Model, UserMixin): 
    # Includes columns for the id, name, username, and password.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    username = db.Column(db.String(32), nullable=True)
    password = db.Column(db.String(32), nullable=True)

    # DB relationships with the todos and messages
    messages = db.relationship('Message', foreign_keys='Message.receiving_user', backref='user_messages', lazy=True)
    todos = db.relationship('ToDo', backref='user_todos', lazy=True)

    # Generate a password hash then set it to its password field
    def set_password(self, password):
        self.password = generate_password_hash(password)

    # Checks whether the plaintext password matches the hashed one in the SQL database
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    # Returns a string representation of the user when queried
    def __repr__(self):
        return f'<user {self.id} : {self.username}>'
    
# Message table
class Message(db.Model):
    # Includes columns for the id, subject, body, and the timestamp.
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(256), nullable=True) 
    body = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, nullable=False)
    filePath = db.Column(db.String(1000), nullable=True)
    recycled = db.Column(db.Boolean, default=False)

    # Include columns for the sending and receiving user.
    sending_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    receiving_user = db.Column(db.Integer, db.ForeignKey('user.id'))

    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))


    def __repr__(self):
        return f'{self.id} : {self.subject}'

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

# To-Do table
class ToDo(db.Model):
    # Includes columns for the description, whether it is done, and who created the task.
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(1000), nullable=False)
    done = db.Column(db.Boolean, default=False)

    user = db.Column(db.Integer, db.ForeignKey('user.id'))

# Deleted accounts database
class DeletedAccounts(db.Model):
    # Fields consisting of the id and username
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)

    # Function to validate whether the username is unique (checks the deleted accounts table)
    def validateUsername(username):
        if DeletedAccounts.query.filter_by(username=username).first() == None:
            return True
        else:
            return False

class Drafts(db.Model):
     # Includes columns for the id, subject, body, and the timestamp.
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(256), nullable=False) 
    body = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, nullable=False)
    filePath = db.Column(db.String(1000), nullable=True)

    # Include columns for the sending and receiving user.
    sending_user = db.Column(db.Integer)
    receiving_user = db.Column(db.Integer)

    # Visiblity
    visible = db.Column(db.Boolean, default=True)


# Categories table 
class Categories(db.Model):
    # Includes the id for the category, the category name, the user associated with the category, and the messages associated with that category
    id = db.Column(db.Integer, primary_key=True)
    categoryName = db.Column(db.String(100))
    userID = db.Column(db.Integer)
    messages = db.relationship('Message', backref='message_category', lazy=True)
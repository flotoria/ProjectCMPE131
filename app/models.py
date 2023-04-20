from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(32), nullable=False)
    
    def set_password(self, password):
        self.password = generate_password_hash(self.password, password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def __repr__(self):
        return f'<user {self.id} : {self.username}>'
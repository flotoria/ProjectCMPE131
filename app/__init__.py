from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager
from flask_socketio import SocketIO, send


app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")


basedir = os.path.abspath(os.path.dirname(__file__))

app.config.from_mapping(
    SECRET_KEY = 'test',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False, 
    UPLOAD_FOLDER = os.path.join(basedir, 'static\image_database'),
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024
)

db = SQLAlchemy(app)

login = LoginManager(app)

login.login_view = 'login'

from app import routes, models
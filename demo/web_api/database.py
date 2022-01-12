from typing import NoReturn
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = None
bcrypt_loground = None

def init_app(app):
    global bcrypt, bcrypt_loground
    
    db.init_app(app)
    bcrypt = Bcrypt(app)
    bcrypt_loground = app.config.get('BECRYPT_LOG_ROUNDS')
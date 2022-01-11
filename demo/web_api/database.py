from typing import NoReturn
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = NoReturn

def init_app(app):
    global bcrypt
    
    db.init_app(app)
    bcrypt = Bcrypt(app)
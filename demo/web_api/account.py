from app import app
from database import db, bcrypt

class Account(db.Model):
    __tablename__ = 'tbl_account'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, password, admin=False) -> None:
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password,
            app.config.get('BECRYPT_LOG_ROUNDS')).decode()

        self.admin = admin

    def __repr__(self) -> str:
        return f"Model: {self.parameter}"
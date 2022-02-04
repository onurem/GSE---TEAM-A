from typing import Tuple
import sqlalchemy
from sqlalchemy.orm.session import Session
from sqlalchemy import select
from database import db, bcrypt, bcrypt_loground

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
            bcrypt_loground).decode()

        self.admin = admin

    def __repr__(self) -> str:
        return f"Model: {self.parameter}"

    def exist(self):
        with Session(db.engine) as session:
            q = session.query(Account).filter(Account.email == self.email)
            return session.query(q.exists()).scalar()

    def get(self):
        with Session(db.engine) as session:
            return session.query(Account).filter_by(email=self.email).one()

    @staticmethod
    def get(email: str):
        try:
            with Session(db.engine) as session:
                return session.query(Account).filter_by(email=email).one()
        except sqlalchemy.exc.NoResultFound:
            return None

    @staticmethod
    def get_by_id(id: int):
        try:
            with Session(db.engine) as session:
                return session.query(Account).filter_by(id=id).one()
        except sqlalchemy.exc.NoResultFound:
            return None

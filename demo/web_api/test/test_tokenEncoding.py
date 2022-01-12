import os
from flask import Flask
from sqlalchemy.orm.session import Session
from account import Account
from test_createDevFlask import TestDevFlask
from my_utils import TokenUtils


class TestTokenEncode(TestDevFlask):
    def setup_class(self):
        TestDevFlask.setup_class(self)
        self.token_utils = TokenUtils(self.app)

    def test_encoding(self):
        user = Account('test8@company', '123456test')

        with self.app.app_context():
            with Session(self.db.engine) as session:
                if not user.exist():
                    session.add(user)
                    session.commit()

                user = user.get()

        print('Mock user = %s' % user.id)
        auth_token = self.token_utils.encode_auth_token(user.id)

        assert isinstance(auth_token, str)


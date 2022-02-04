from datetime import date, datetime, timedelta
import jwt
from flask import Flask


def convert_pg_uri(old_uri: str) -> str:
    if 'postgres:' in old_uri:
        return old_uri.replace('postgres', 'postgresql')
    else:
        return old_uri


class TokenUtils:

    def __init__(self, app: Flask) -> None:
        self.app = app

    def encode_auth_token(self, user_id: str) -> str:
        """
            Generate the authen token
            :return: string
        """
        payload = {
            'exp': datetime.utcnow() + timedelta(days=0, hours=5),
            'iat': datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            self.app.config.get('SECRET_KEY'),
            algorithm='HS256'
        )

    def decode_auth_token(self, auth_token):
        """
            Decode the authen token
            :return: string
        """
        try:
            payload = jwt.decode(
                auth_token,
                self.app.config.get('SECRET_KEY'),
                algorithms=["HS256"])

            return payload, ''
        except jwt.ExpiredSignatureError:
            return None, 'Signature expired. Please login again'
        except jwt.InvalidTokenError:
            return None, f'Invalid token, auth_token={auth_token}'

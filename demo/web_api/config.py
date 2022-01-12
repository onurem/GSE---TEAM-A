import os

from my_utils import convert_pg_uri
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'simple_secret'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  #Suppress SQLALCHEMY_TRACK_MODIFICATIONS warns
    SQLALCHEMY_DATABASE_URI = convert_pg_uri(os.environ.get('DATABASE_URL',
                       'postgresql://localhost:5432/hateless_dev?user=dev_user&password=abc123456')
    )

    def __repr__(self) -> str:
        return f"Config: {self.__dict__}"


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = False

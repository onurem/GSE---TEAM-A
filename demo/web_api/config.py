import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'simple_secret'
    SQLALCHEMY_DATABASE_URI = os.environ \
        .get('DATABASE_URL', 'postgresql://localhost:5432/hateless_dev?user=dev_user&password=abc123456')


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = False

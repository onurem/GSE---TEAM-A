import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

class TestDevFlask:
    def setup_class(self):
        config_file = os.environ.get("APP_SETTINGS", "config.StagingConfig")

        self.app = Flask(__name__)
        self.app.config.from_object(config_file)
        self.db = SQLAlchemy(self.app)

    def test_create_app(self):
        print('\nSECRET_KEY = %s' % self.app.config['SECRET_KEY'])
        assert self.app.config['SECRET_KEY'] == 'simple_secret'

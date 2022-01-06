from flask.json import load
from app import app, load_model

if __name__ == "__main__":
    load_model()
    app.run()
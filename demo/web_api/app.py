import logging
import os

import json
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

from langdetect import detect

from models.model_manager import ModelManager
import database
import commands

app = Flask(__name__, static_folder='static/static', template_folder='static')
config_file = os.environ.get("APP_SETTINGS", "config.StagingConfig")
app.config.from_object(config_file)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
cors = CORS(app)


database.init_app(app)
commands.init_app(app)

app.logger.setLevel(logging.INFO)
MODEL_MANAGER = None

@app.before_first_request
def on_start():
    global config_file
    logger = app.logger
    logger.info("Event handler on start is running")
    logger.info('Config loaded, name=%s\nproperties=%s', config_file, app.config)

    global MODEL_MANAGER
    MODEL_MANAGER = ModelManager('models', logger)
    MODEL_MANAGER.load_all_models()


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/admin/models')
def list_models():
    """
        List available models in memory
    """
    global MODEL_MANAGER
    return jsonify(list(MODEL_MANAGER.models.keys()))


@app.route('/<version>/predict', methods=['POST'])
def predict(version):
    logger = app.logger
    global model_manager

    msg = ""

    classifier, vectorizer = MODEL_MANAGER.models.get(version, None)

    if classifier is not None:
        try:
            msg = request.form['message']
            logger.info('Processing %s', msg)

            msg_lang = detect(msg)
            assert msg_lang, 'en'

            w_vect = vectorizer.transform([msg])
            pred = classifier.predict_proba(w_vect.reshape(1, -1))[0]

            return jsonify(pred.tolist())

        except AssertionError as error:
            return f'Language message is not EN, err={error}', 400

    return 'No model found'

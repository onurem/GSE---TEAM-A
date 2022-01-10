import glob
import logging
from flask import Flask, request, jsonify, render_template
from langdetect import detect
from flask_cors import cross_origin, CORS

from models.model_manager import ModelManager

app = Flask(__name__, static_folder='static/static', template_folder='static')
app.logger.setLevel(logging.INFO)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

MODEL_MANAGER = None

@app.before_first_request
def on_start():
    logger = app.logger
    logger.info("on_start run")

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

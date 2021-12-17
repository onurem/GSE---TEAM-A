import logging

import os
import glob
import pickle
from flask import Flask, request, jsonify
from langdetect import detect

logging.basicConfig(level="INFO", format="[%(name)s] %(message)s")

app = Flask(__name__)
models = {}
vtrizers = {}


@app.route('/', methods=['GET'])
def index():
    return "<h1>Welcome to Hateless</h1>"


@app.route('/<version>/predict', methods=['POST'])
def predict(version):
    msg = ""
    model = models.get(version, None)
    vectorizer = vtrizers.get(version, None)

    if model is not None:
        try:
            msg = request.form['message']
            logging.info('processing %s', msg)
            lang = detect(msg)
            assert lang, 'en'

            w_vect = vectorizer.transform([msg])
            pred = models['v0'].predict_proba(w_vect.reshape(1, -1))[0]
            logging.info('Result=%s', pred)
            return 'Good'

        except AssertionError as error:
            logging.error("Failed to process msg=%s, reason=%s", msg, error)
            return jsonify(err=f'Failed to classify, msg={msg}, reason={error}')

    return 'No model found'


def get_path_model(filename):
    PATH_TO_MODELS = 'models'
    return os.path.join(PATH_TO_MODELS, filename)


def load_model():
    logging.info('== Loading classifiers ==')

    try:
        if len(models) == 0:
            models['v0'] = pickle.load(
                open(
                    get_path_model('hateless_v0.pkl'), 'rb'))

            vtrizers['v0'] = pickle.load(
                open(
                    get_path_model('vectorizer_v0.pkl'), 'rb'))
    except Exception as err:
        logging.error('Failed to process file %s', err)

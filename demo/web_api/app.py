import os
import glob
import pickle
from flask import Flask, request, jsonify, render_template
from langdetect import detect
from flask_cors import cross_origin, CORS

app = Flask(__name__, static_folder='static/static', template_folder='static')
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

logger = app.logger

def get_path_model(filename):
    PATH_TO_MODELS = 'models'
    return os.path.join(PATH_TO_MODELS, filename)


def load_model():
    logger.info('== Loading classifiers ==')

    try:
        if len(models) == 0:
            models['v0'] = pickle.load(
                open(
                    get_path_model('hateless_v0.pkl'), 'rb'))

            vtrizers['v0'] = pickle.load(
                open(
                    get_path_model('vectorizer_v0.pkl'), 'rb'))
    except Exception as err:
        logger.error('Failed to process file %s', err)


models = {}
vtrizers = {}
load_model()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/<version>/predict', methods=['POST'])
def predict(version):
    msg = ""
    model = models.get(version, None)
    vectorizer = vtrizers.get(version, None)

    if model is not None:
        try:
            msg = request.form['message']
            logger.info('processing %s', msg)
            lang = detect(msg)
            assert lang, 'en'

            w_vect = vectorizer.transform([msg])
            pred = models['v0'].predict_proba(w_vect.reshape(1, -1))[0]
            return jsonify(pred.tolist())

        except AssertionError as error:
            logger.error("Failed to process msg=%s, reason=%s", msg, error)
            return f'Failed to classify, msg={msg}, reason={error}', 400

    return 'No model found'

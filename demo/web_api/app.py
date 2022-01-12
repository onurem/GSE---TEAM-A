from functools import wraps
import logging
import os

from flask import Flask, request, jsonify, render_template
from flask.helpers import make_response
from flask_cors import CORS

from langdetect import detect
from account import Account
from trainer.Prediction import Prediction
from trainer.Predictor import Predictor
from my_utils import TokenUtils

from models.model_manager import ModelManager
import database
import commands

app = Flask(__name__, static_folder='static/static', template_folder='static')
config_file = os.environ.get("APP_SETTINGS", "config.StagingConfig")
app.config.from_object(config_file)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
cors = CORS(app)
auth_utils = TokenUtils(app)

database.init_app(app)
commands.init_app(app)

app.logger.setLevel(logging.INFO)
MODEL_MANAGER:ModelManager = None

@app.before_first_request
def on_start():
    global config_file
    logger = app.logger
    logger.info("Event handler on start is running")
    logger.info('Config loaded, name=%s\nproperties=%s',
                config_file, app.config)

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


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({
                'status': 'fail',
                'message': 'Missing token!'
            }), 401

        current_user = None
        try:
            payload, err_msg = auth_utils.decode_auth_token(token)

            if payload:
                current_user = Account.get_by_id(payload['sub'])

            if current_user is None:
                return jsonify({
                    'status': 'fail',
                    'message': f'Invalid token! Reason={err_msg}'
                }), 401

        except Exception:
            return jsonify({
                'status': 'fail',
                'message': 'Failed to decode token'
            }), 401

        return f(current_user, *args, **kwargs)

    return decorated


@app.route('/auth/login', methods=['POST'])
def auth_login():
    email = request.form['email']
    password = request.form['password']

    try:
        account = Account.get(email)
        if (account is not None) and (database.bcrypt.check_password_hash(
            account.password,
            password
        )):
            auth_token = auth_utils.encode_auth_token(account.id)
            if auth_token:
                res = {
                    'status': 'success',
                    'message': 'Succesful logged in',
                    'auth_token': auth_token
                }

                return jsonify(res), 200

        res = {
            'status': 'fail',
            'message': 'user not exist or auth token encoding failed'
        }

        return jsonify(res), 404
    except Exception as e:
        app.logger.error('Unexpected error = %s, msg=%s', e.__class__, e)
        res = {
            'status': 'fail',
            'message': f'Unexpected error {e}'
        }
        return jsonify(res), 500


@app.route('/auth/validate', methods=['GET'])
@token_required
def auth_validate(current_user: Account):
    return jsonify({
        'status': 'success',
        'message': f'welcome {current_user.email}'
    })

@app.route('/<version>/predict', methods=['POST'])
def predict(version):
    logger = app.logger
    global model_manager

    msg = ""

    # classifier, vectorizer = MODEL_MANAGER.models.get(version, None)
    predictor: Predictor = MODEL_MANAGER.predictor_factory.get_predictor(version)

    if predictor is not None:
        try:
            msg = request.form['message']
            logger.info('Processing %s', msg)

            msg_lang = detect(msg)
            assert msg_lang, 'en'

            rs: Prediction = predictor.predict(msg)

            return jsonify({
                'label': rs.predicted_class,
                'confidences': rs.confidences
            }), 200

        except AssertionError as error:
            return f'Language message is not EN, err={error}', 400

    return 'No model found'

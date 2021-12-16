import logging

from flask import Flask, request, jsonify
from langdetect import detect

logging.basicConfig(level="INFO", format="[%(name)s] %(message)s")

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "<h1>Welcome to Hateless</h1>"

@app.route('/predict', methods=['POST'])
def predict():
    msg = ""
    try:
        if request.method != "POST":
            return jsonify(err='Invalid request')

        msg = request.form['message']
        lang = detect(msg)
        assert lang, 'en'

    except AssertionError as error:
        logging.error("Failed to process msg=%s, reason=%s", msg, error)
        return jsonify(err=f'Failed to classify, msg={msg}, reason={error}')
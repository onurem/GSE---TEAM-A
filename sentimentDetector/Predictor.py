import pickle
import pandas as pd
from sklearn.metrics import accuracy_score

from ModelTrainer import ModelTrainer


class Predictor:

    def __init__(self, model_path, vectorizer_path):
        self.tfidf_vect = pickle.load(open(vectorizer_path, 'rb'))
        self.clf = pickle.load(open(model_path, 'rb'))

    def predict(self, message: str):
        transformed = self.tfidf_vect.transform([message])
        return self.clf.predict(transformed)

import pickle
from sklearn.svm import LinearSVC

from sentimentDetector.Prediction import Prediction


class Predictor:
    clf: LinearSVC

    def __init__(self, model_path: str, vectorizer_path: str):
        self.tfidf_vect = pickle.load(open(vectorizer_path, 'rb'))
        self.clf = pickle.load(open(model_path, 'rb'))

    def predict(self, message: str) -> Prediction:
        """Predicts the class of a string (e.g. offensive speech)
        The classes are determined by model and vectorizer

        :param message: str
            The text that should be predicted
        :returns:
        Prediction
            A prediction object holding the most likely class and
            confidences for each class
        """
        transformed = self.tfidf_vect.transform([message])
        predicted_class: str = self.clf.predict(transformed)
        raw_scores = self.clf._predict_proba_lr(transformed)
        scores = raw_scores[0]
        labeled_scores = dict(zip(self.clf.classes_, scores))
        return Prediction(predicted_class, labeled_scores)

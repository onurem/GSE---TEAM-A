import pickle
from sklearn.svm import LinearSVC


class Predictor:
    clf: LinearSVC

    def __init__(self, model_path, vectorizer_path):
        self.tfidf_vect = pickle.load(open(vectorizer_path, 'rb'))
        self.clf = pickle.load(open(model_path, 'rb'))

    def predict(self, message: str):
        transformed = self.tfidf_vect.transform([message])
        prediction = self.clf.predict(transformed)
        raw_scores = self.clf._predict_proba_lr(transformed)
        scores = raw_scores[0]
        labeled_scores = dict(zip(self.clf.classes_, scores))
        return prediction, labeled_scores

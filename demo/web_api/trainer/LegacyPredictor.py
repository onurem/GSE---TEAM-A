import pickle
from sklearn.svm import LinearSVC
from trainer.Predictor import Predictor
from trainer.Prediction import Prediction

class LegacyPredictor(Predictor):
    clf = None
    CLASSES = []

    def get_class(x):
        if x == 0:
            return 'hate_speech'
        elif x == 1:
            return 'offensive_language'
        else:
            return 'neither'

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
        predicted_class: str = LegacyPredictor.get_class(self.clf.predict(transformed)[0])
        raw_scores = self.clf.predict_proba(transformed.reshape(1, -1))
        scores = raw_scores[0]
        labeled_scores = dict(zip([LegacyPredictor.get_class(x) for x in self.clf.classes_.tolist()], scores.tolist()))
        return Prediction(predicted_class, labeled_scores)
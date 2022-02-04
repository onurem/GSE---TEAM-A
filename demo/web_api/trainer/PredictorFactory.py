from trainer.Predictor import Predictor
from trainer.LegacyPredictor import LegacyPredictor

class PredictorFactory:
    predictor_map = {}

    def add_predictor(self, model_ver: str, clf, vt):
        response_predictor = Predictor(clf, vt, None)
        if model_ver == 'v0':
            response_predictor = LegacyPredictor(clf, vt, None)
        
        self.predictor_map[model_ver] = response_predictor

    def get_predictor(self, model_ver: str) -> Predictor:
        return self.predictor_map.get(model_ver)
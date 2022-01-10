class Prediction:
    def __init__(self, predicted_class: str, confidences: dict[str, float]):
        self.predicted_class = predicted_class
        self.confidences = confidences

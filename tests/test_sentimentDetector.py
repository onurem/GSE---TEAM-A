#!/usr/bin/env python
import os
import pandas as pd

from demo.web_api.ModelTrainer import ModelTrainer
from demo.web_api.Predictor import Predictor


class TestSentimentDetector:

    def setup_class(self):
        self.script_root = os.path.dirname(__file__)
        self.training_path = os.path.join(self.script_root, 'testdata/test.csv')
        self.model_path = os.path.join(self.script_root, '../resources/test_model.pkl')
        self.vectorizer_path = os.path.join(self.script_root, '../resources/test_vect.pkl')

    def teardown_method(self):
        if os.path.exists(self.model_path):
            os.remove(self.model_path)
        if os.path.exists(self.vectorizer_path):
            os.remove(self.vectorizer_path)

    def test_load_data(self):
        small_set_path = os.path.join(self.script_root, 'testdata/small_set_classified.csv')
        classified_set_path = os.path.join(self.script_root, 'testdata/small_set_classified.csv')
        trainer = ModelTrainer(small_set_path)
        actual_data = pd.read_csv(classified_set_path)

        result = trainer.read_data()

        pd.testing.assert_frame_equal(actual_data, result)

    def test_can_save_model(self):
        trainer = ModelTrainer(self.training_path)

        trainer.train_model(self.model_path, self.vectorizer_path)

        assert os.path.exists(self.model_path)
        assert os.path.exists(self.vectorizer_path)

    def test_can_use_saved_two_class_model(self):
        trainer = ModelTrainer(self.training_path)
        trainer.train_model(self.model_path, self.vectorizer_path)
        predictor = Predictor(self.model_path, self.vectorizer_path)

        result = predictor.predict('Unknown fine text')

        assert result.predicted_class == 'neither'
        confidence = result.confidences
        assert confidence['neither'] > 0
        assert confidence['hate_speech'] >= 0
        assert confidence['neither'] > confidence['hate_speech']
        assert os.path.exists(self.model_path)
        assert os.path.exists(self.vectorizer_path)

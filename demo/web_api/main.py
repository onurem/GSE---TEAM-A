#!/usr/bin/env python
import os
from ModelTrainer import ModelTrainer
from Predictor import Predictor


def main():
    model_path = 'senti_svc_model.pkl'
    vectorizer_path = 'tfidf_vect.transform.pkl'
    if os.path.exists(model_path):
        os.remove(model_path)
    if os.path.exists(vectorizer_path):
        os.remove(vectorizer_path)

    script_root = os.path.dirname(__file__)
    training_path = os.path.join(script_root, '../resources/training_data.csv')
    trainer = ModelTrainer(training_path)
    trainer.train_model(model_path, vectorizer_path)

    texts = [
        'This may be some hatespeech',
        'This may be fine text',
        'Another text for testing'
    ]

    predictor = Predictor(model_path, vectorizer_path)
    for text in texts:
        print("============Trying out with text==============")
        print(text)
        prediction = predictor.predict(text)
        print(prediction.predicted_class)
        print(prediction.confidences)


if __name__ == '__main__':
    main()

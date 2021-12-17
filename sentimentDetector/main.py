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

    trainer = ModelTrainer()
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
        prediction, scores = predictor.predict(text)
        print(prediction)
        print(scores)


if __name__ == '__main__':
    main()

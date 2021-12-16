#!/usr/bin/env python
import os
from ModelTrainer import ModelTrainer


def main():
    model_path = 'senti_svc_model.pkl'
    vectorizer_path = 'tfidf_vect.transform.pkl'
    if os.path.exists(model_path):
        os.remove(model_path)
    if os.path.exists(vectorizer_path):
        os.remove(vectorizer_path)

    trainer = ModelTrainer()
    trainer.train_model(model_path, vectorizer_path)


if __name__ == '__main__':
    main()

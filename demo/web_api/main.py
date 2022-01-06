#!/usr/bin/env python
import os
from ModelTrainer import ModelTrainer


def main():
    if(os.path.exists('senti_svc_model.pkl')):
        os.remove('senti_svc_model.pkl')
    trainer = ModelTrainer()
    trainer.train_model()


if __name__ == '__main__':
    main()

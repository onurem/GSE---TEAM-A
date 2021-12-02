#!/usr/bin/env python
import os
from ModelTrainer import ModelTrainer


def main():
    os.remove('senti_svc_model.pkl')
    trainer = ModelTrainer()
    trainer.train_model()


if __name__ == '__main__':
    main()

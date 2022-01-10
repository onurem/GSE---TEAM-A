import logging
import os
import glob
import re
import pickle
from typing import Tuple
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer

class ModelManager:
    """
        To load/check availability of pickled models
    """

    def __init__(self, models_path: str, logger: logging.Logger) -> None:
        """
            Constructor for ModelManager
        """
        self.models = {}
        self.path_to_models = models_path
        self.logger = logger

    def get_path_model(self, filename: str) -> str:
        """
            Get full path to model
        """
        return os.path.join(self.path_to_models, filename)

    def read_model(self, version) -> Tuple[LinearSVC, TfidfVectorizer]:
        """
            Unpickle SVC and Vectorizer pair
        """
        return (pickle.load(open(self.get_path_model(f'hateless_{version}.pkl'), 'rb')),
                pickle.load(open(self.get_path_model(f'vectorizer_{version}.pkl'), 'rb')))

    def load_model(self, version):
        """
            Load version to memory
        """
        logger = self.logger
        models = self.models

        try:
            models[version] = self.read_model(version)
            logger.info('Loaded version=%s', version)

        except pickle.UnpicklingError as err:
            logger.error('Failed unpickling, version=%s, err=%s', version, err)

    def load_all_models(self):
        """
            Load all versions available on disk
        """
        ver_matcher = r'\_(v\d+\_*\d*)\.pkl'   # version matcher

        for f in glob.glob(self.get_path_model('hateless_v*.pkl')):
            f_name = os.path.basename(f)
            version = re.search(ver_matcher, f_name).group(1)

            if version is None:
                self.logger.info('Invalid version, path=%s', f_name)
                continue

            # Check if the pair exists
            vt_model = f.replace('hateless', 'vectorizer')
            if os.path.isfile(vt_model):
                self.load_model(version)

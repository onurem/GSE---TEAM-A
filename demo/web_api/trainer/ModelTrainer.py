import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score


class ModelTrainer:

    def __init__(self, path_to_training_data):
        self.path_to_training_data = path_to_training_data

    def read_data(self) -> pd.DataFrame:
        """Loads the configured data

        :returns:
        DataFrame
            A pandas DataFrame holding the file's data
        """
        df = pd.read_csv(self.path_to_training_data)
        return df

    def train_model(self, model_path: str, vectorizer_path: str) -> None:
        """Trains a model and a vectorizer

        :param model_path: str
            Path to where the model will be stored
        :param vectorizer_path: str
            Path to where the according vectorizer will be stored
        """
        text_col = 'tweet'
        label = 'class'

        df = self.read_data()

        tfidf_vector = TfidfVectorizer(ngram_range=(1, 2),
                                       min_df=10,
                                       max_df=0.3,
                                       lowercase=True,
                                       stop_words=None)

        x_tfidf = tfidf_vector.fit_transform(df[text_col])

        x = x_tfidf
        y = df[label]

        test_size = 0.2
        x_train, x_test, y_train, y_test = self._split_train_test(test_size, x, y)

        df['train_test'] = pd.Series(df.index.isin(y_test.index)).map(lambda is_test: 'Test' if is_test else 'Train')

        print(f'Training on column {label}')
        clf = self._train_classifier(x_train=x_train,
                                     x_test=x_test,
                                     x=x,
                                     y_train=y_train,
                                     y_test=y_test,
                                     y=y)

        pickle.dump(clf, open(model_path, 'wb'))
        pickle.dump(tfidf_vector, open(vectorizer_path, 'wb'))

    # region private functions

    @staticmethod
    def _classification(x) -> str:
        if x == 0:
            return "hate_speech"
        if x == 1:
            return "offensive_language"
        if x == 2:
            return "neither"

    @staticmethod
    def _score(classifier, x_test, x_train, x, y_test, y_train, y) -> None:
        y_test_pred = classifier.predict(x_test)
        y_train_pred = classifier.predict(x_train)
        y_pred = classifier.predict(x)

        print(f"Classifier: {classifier.__class__}\n")

        print('Accuracy Summary')
        print('================')

        print(f'Test:    {accuracy_score(y_test, y_test_pred) * 100:6.2f}%')
        print(f'Train:   {accuracy_score(y_train, y_train_pred) * 100:6.2f}%')
        print(f'Overall: {accuracy_score(y, y_pred) * 100:6.2f}%')

    def _train_classifier(self, x_train, x_test, x, y_train, y_test, y) -> LinearSVC:

        clf = LinearSVC(C=1.0, max_iter=10000)

        clf.fit(x_train, y_train)

        print("Done.")
        self._score(clf, x_test, x_train, x, y_test, y_train, y)
        return clf

    @staticmethod
    def _split_train_test(test_size: float, x, y):
        if test_size > 0.0:
            return train_test_split(x, y,
                                    test_size=test_size,
                                    stratify=y,
                                    random_state=43
                                    )
        else:
            return x, None, y, None

    # endregion

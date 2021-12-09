import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score


class ModelTrainer:

    @staticmethod
    def read_data():
        return pd.read_csv("resources/auto_labled_data.csv")

    @staticmethod
    def classification(x):
        if x == 0:
            return "hate_speech"
        if x == 1:
            return "offensive_language"
        if x == 2:
            return "neither"

    @staticmethod
    def score(classifier, x_test, x_train, x, y_test, y_train, y):
        y_test_pred = classifier.predict(x_test)
        y_train_pred = classifier.predict(x_train)
        y_pred = classifier.predict(x)

        print(f"Classifier: {classifier.__class__}\n")

        print('Accuracy Summary')
        print('================')

        print(f'Test:    {accuracy_score(y_test, y_test_pred) * 100:6.2f}%')
        print(f'Train:   {accuracy_score(y_train, y_train_pred) * 100:6.2f}%')
        print(f'Overall: {accuracy_score(y, y_pred) * 100:6.2f}%')

    def train_classifier(self, x_train, x_test, x, y_train, y_test, y):

        clf = LinearSVC(C=1.0, max_iter=10000)

        clf.fit(x_train, y_train)

        print("Done.")
        self.score(clf, x_test, x_train, x, y_test, y_train, y)
        return clf

    @staticmethod
    def split_train_test(test_size, x, y):
        if test_size > 0.0:
            return train_test_split(x, y,
                                    test_size=test_size,
                                    stratify=y,
                                    random_state=43
                                    )
        else:
            return x, None, y, None

    def train_model(self, model_path, vectorizer_path):
        text_col = 'tweet'
        label = 'class'

        df = self.read_data()
        df['class'] = df['class'].apply(self.classification)
        df = df.drop(columns=['Unnamed: 0', 'count', 'hate_speech', 'offensive_language', 'neither'])

        tfidf_vector = TfidfVectorizer(ngram_range=(1, 2),
                                       min_df=10,
                                       max_df=0.3,
                                       lowercase=True,
                                       stop_words=None)

        x_tfidf = tfidf_vector.fit_transform(df[text_col])

        x = x_tfidf
        y = df[label]

        test_size = 0.2
        x_train, x_test, y_train, y_test = self.split_train_test(test_size, x, y)

        df['train_test'] = pd.Series(df.index.isin(y_test.index)).map(lambda is_test: 'Test' if is_test else 'Train')

        print(f'Training on column {label}')
        clf = self.train_classifier(x_train=x_train,
                                    x_test=x_test,
                                    x=x,
                                    y_train=y_train,
                                    y_test=y_test,
                                    y=y)

        pickle.dump(clf, open(model_path, 'wb'))
        pickle.dump(tfidf_vector, open(vectorizer_path, 'wb'))

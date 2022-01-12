import pandas as pd
import numpy as np
import warnings
import logging
import pickle
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer

warnings.filterwarnings('ignore')

pd.options.display.max_columns = 30
pd.options.display.max_rows = 200
pd.options.display.float_format = '{:.2f}'.format
pd.options.display.max_colwidth = 200  # default 50; None = all

np.set_printoptions(suppress=True)  # no scientific notation for small numbers


########################################################


logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', level=logging.INFO)

logging.getLogger().setLevel(logging.WARNING)
logging.getLogger().info("Logging INFOS.")
logging.getLogger().warning("Logging WARNINGS.")
logging.getLogger().error("Logging ERRORS.")

np.set_printoptions(suppress=True)


training_df = pd.read_csv("../../resources/training_data.csv")
tfidf_vect = TfidfVectorizer(ngram_range=(1, 2),
                             min_df=10,
                             max_df=0.3,
                             lowercase=True,
                             stop_words=None)

text_col = 'tweet'
label = 'class'

X_tfidf = tfidf_vect.fit_transform(training_df[text_col])

X = X_tfidf
y = training_df[label]
test_size = 0.2

if test_size > 0.0:
    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size=test_size,
                                                        stratify=y,
                                                        random_state=43
                                                        )
else:
    X_train, X_test, y_train, y_test = X, None, y, None

training_df['train_test'] = pd.Series(
    training_df.index.isin(y_test.index)).map(
    lambda x: 'Test' if x else 'Train')
print("Trainigsmatrix:", X_train.shape)
print("Testmatrix:    ", X_test.shape)

parameters = {
    'penalty': ['l1', 'l2'],
    'loss': ['hinge', 'squared_hinge'],
    'dual': [True, False],
    'C': [0.1, 1.0, 10.0],
    'multi_class': ['ovr', 'crammer_singer'],
    'max_iter': [10, 20, 30, 50, 100],
    'random_state': [43]
}

clf = LinearSVC()

f1_scorer = make_scorer(f1_score, pos_label='H', average='weighted')

grid_obj = GridSearchCV(clf,
                        scoring=f1_scorer,
                        param_grid=parameters,
                        cv=5)

grid_obj = grid_obj.fit(X_train, y_train)

# Get the estimator
clf = grid_obj.best_estimator_
print(clf)
print(grid_obj.best_params_)

pickle.dump(clf, open('../../resources/tuned_svc_model.pkl', 'wb'))
pickle.dump(tfidf_vect, open('../../resources/tuned_svc_tfidf_vect.pkl', 'wb'))

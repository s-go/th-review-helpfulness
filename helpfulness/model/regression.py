'''
Probabilistic SVM-regression model for predicting review helpfulness
inspired by Kim et al. (2006).
'''
import time

from sklearn.metrics.scorer import make_scorer
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR

from helpfulness.data.preprocess import FIELDNAMES
from helpfulness.model.evaluation import plain_pearsonr
from helpfulness.model.features import compute_helpfulness_score
import pandas as pd


class ReviewHelpfulnessRegressionModel:

    def __init__(self, reviews_csv_filepath):
        self.reviews_dataframe = self._get_dataframe(reviews_csv_filepath)
        self._model = SVR()

    def _get_dataframe(self, csv_filepath):
        '''
        Converts the given CSV file into a pandas ``DataFrame``.
        '''
        with open(csv_filepath) as csv_file:
            return pd.read_csv(
                csv_file, header=None, names=FIELDNAMES,
                converters={'helpful': eval}
            )

    def get_feature_matrix(self):
        '''
        Returns the feature matrix of the model.
        '''
        # TODO: Use more features
        return self.reviews_dataframe.as_matrix(['overall'])

    def get_target_vector(self):
        return self.reviews_dataframe['helfulnessScore']

    def get_train_test_sets(self):
        '''
        Splits the dataset into training and test set (90%/10%).

        Returns ``(X_train, X_test, y_train, y_test)`` tuple.
        '''
        X = self.get_feature_matrix()
        y = self.get_target_vector()

        return train_test_split(X, y, test_size=0.1, random_state=42)

    def extract_features(self):
        self.reviews_dataframe['helfulnessScore'] = \
            self.reviews_dataframe['helpful'].apply(compute_helpfulness_score)

    def tune_hyper_params_kfold(self):
        '''
        Tunes the hyper-parameters of the model by performing a full-grid
        search and 10-fold cross-validation (slow!).
        '''
        X = self.get_feature_matrix()
        y = self.get_target_vector()
        kf = KFold(n_splits=10, shuffle=True, random_state=4)
        kf.get_n_splits(X)

        # TODO: Learn optimal kernel
        # TODO: Learn optimal parameters
        param_grid = [
            {'C': [0.1, 0.5]},
            {
                'C': [1, 10, 100, 1000],
                'gamma': [0.001, 0.0001],
                'kernel': ['rbf']
            },
        ]
        pearsonr_scorer = make_scorer(plain_pearsonr)
        self._model = GridSearchCV(
            self._model, param_grid, cv=5, scoring=pearsonr_scorer, n_jobs=1)

        print('# Tuning hyper-parameters on development set...')
        [self._model.fit(X[train], y[train]).score(X[test], y[test])
         for train, test in kf.split(X)]

        print('Best parameters set found:', self._model.best_params_)
        print('Fit Pearson r:', self._model.best_score_)

    def tune_hyper_params(self):
        '''
        Tunes the hyper-parameters of the model by performing a full-grid
        search.
        '''
        X_train, X_test, y_train, y_test = self.get_train_test_sets()

        # TODO: Learn optimal kernel
        # TODO: Learn optimal parameters
        param_grid = [
            {'C': [0.1, 0.5]},
            {
                'C': [1, 10, 100, 1000],
                'gamma': [0.001, 0.0001],
                'kernel': ['rbf']
            },
        ]
        pearsonr_scorer = make_scorer(plain_pearsonr)
        self._model = GridSearchCV(
            self._model, param_grid, cv=5, scoring=pearsonr_scorer, n_jobs=1)

        print('# Tuning hyper-parameters on development set...')
        self._model.fit(X_train, y_train).score(X_test, y_test)
        print('Best parameters set found:', self._model.best_params_)
        print('Fit Pearson r:', self._model.best_score_)

    def evaluate_model(self):
        '''
        Evaluates the model performance by performing a 10-fold
        cross-validation on the dataset.
        '''
        # TODO: Parametrize dataset so we can evaluate on CV data after
        # tuning on development data
        X = self.get_feature_matrix()
        y = self.get_target_vector()

        print()
        print('# Starting 10-fold cross-validation...')
        scores = cross_val_score(self._model, X, y, cv=10, n_jobs=-1)
        # TODO: Attention! 95% confidence bounds relative to CV!
        print("CV Pearson r: %0.2f (± %0.2f)" % (
            scores.mean(), scores.std() * 2))

    def run_pipeline(self):
        print('--- Starting experiment ---', end='\n\n')
        start_time = time.time()

        self.extract_features()
        self.tune_hyper_params()
        self.evaluate_model()

        print()
        print("--- Took %0.2f seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    data_path = 'data/reviews_dev.csv'
    # data_path = 'data/reviews_traintest.csv'

    helpfulness_model = ReviewHelpfulnessRegressionModel(data_path)
    helpfulness_model.run_pipeline()

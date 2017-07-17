'''
Probabilistic SVM-regression model for predicting review helpfulness
inspired by Kim et al. (2006).
'''
import time

from sklearn.metrics.scorer import make_scorer
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR

from helpfulness.data.preprocess import FIELDNAMES
from helpfulness.model.evaluation import plain_pearsonr
from helpfulness.model.features import compute_helpfulness_score
from helpfulness.model.features import num_tokens
import pandas as pd


class ReviewHelpfulnessRegressionModel:

    def __init__(self, reviews_csv_filepath):
        self.reviews_dataframe = self._get_dataframe(reviews_csv_filepath)
        print(f'Data path: "{reviews_csv_filepath}" '
              f'({len(self.reviews_dataframe)} reviews)')

        self._model = SVR(kernel='rbf', C=1, gamma=0.001)

    def _get_dataframe(self, csv_filepath):
        '''
        Converts the given CSV file into a pandas ``DataFrame``.
        '''
        with open(csv_filepath) as csv_file:
            return pd.read_csv(
                csv_file, header=None, names=FIELDNAMES,
                converters={'helpful': eval}
            )

    def extract_features(self):
        '''
        Adds features that need to be computed from the raw data to the
        dataframe.
        '''
        print('Extracting features from raw data...')
        # Add number of tokens (LEN)
        self.reviews_dataframe['numTokens'] = \
            self.reviews_dataframe['reviewText'].apply(num_tokens)

        # Add helpfulness score (STR)
        self.reviews_dataframe['helpfulnessScore'] = \
            self.reviews_dataframe['helpful'].apply(compute_helpfulness_score)

    def get_feature_matrix(self):
        '''
        Returns the feature matrix of the model.
        '''
        # TODO: Add Unigram (UGR)
        return self.reviews_dataframe.as_matrix(['overall', 'numTokens'])
        # TODO: Scale each feature between [0, 1]
        # TODO: Apply standard transformation to each feature measurement *f*
        # f = ln(f + 1)?

    def get_scorer(self):
        '''
        Returns a scikit-learn scoring metric that calculates the
        Pearson correlation coefficient.
        '''
        return make_scorer(plain_pearsonr)

    def get_target_vector(self):
        return self.reviews_dataframe['helpfulnessScore']

    def get_train_test_sets(self):
        '''
        Splits the dataset into training and test set (90%/10%).

        Returns ``(X_train, X_test, y_train, y_test)`` tuple.
        '''
        X = self.get_feature_matrix()
        y = self.get_target_vector()

        return train_test_split(X, y, test_size=0.1, random_state=42)

    def fit_model(self):
        X_train, X_test, y_train, y_test = self.get_train_test_sets()
        self._model.fit(X_train, y_train).score(X_test, y_test)

    def tune_hyperparams(self):
        '''
        Tunes the hyperparameters of the model by performing a full-grid
        search.
        '''
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
        self._model = GridSearchCV(
            self._model, param_grid, cv=5, scoring=self.get_scorer(), n_jobs=1)

        print('# Tuning hyperparameters on development set...')
        self.fit_model()
        print('Best parameters set found:', self._model.best_params_)
        print('Fit Pearson r:', self._model.best_score_)

    def evaluate_model(self):
        '''
        Evaluates the model performance by performing a 10-fold
        cross-validation on the dataset.
        '''
        print()
        print('Starting 10-fold cross-validation...')
        print('Model:', self._model)

        X = self.get_feature_matrix()
        y = self.get_target_vector()

        scores = cross_val_score(
            self._model, X, y, cv=10, scoring=self.get_scorer(), n_jobs=-1)
        print()
        # TODO: Attention! 95% confidence bounds relative to CV!
        print("CV Pearson r: %0.2f (± %0.2f)" % (
            scores.mean(), scores.std() * 2))

    def run_pipeline(self):
        print('--- Starting experiment ---', end='\n\n')
        start_time = time.time()

        self.extract_features()
        self.tune_hyperparams()
        self.evaluate_model()

        print()
        print("--- Took %0.2f seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    data_path = 'data/reviews_dev.csv'
    # data_path = 'data/reviews_traintest.csv'

    helpfulness_model = ReviewHelpfulnessRegressionModel(data_path)
    helpfulness_model.extract_features()

    # helpfulness_model.run_pipeline()
    helpfulness_model.evaluate_model()

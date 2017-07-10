'''
Probabilistic SVM-regression model for predicting review helpfulness
borrowing from Kim et al. (2006).
'''
from math import sqrt

from sklearn import svm
from sklearn.model_selection._search import GridSearchCV

from helpfulness.data.preprocess import FIELDNAMES
from helpfulness.model.features import compute_helpfulness_score
import pandas as pd


class ReviewHelpfulnessRegressionModel:

    def __init__(self, reviews_csv_filepath):
        self.reviews_dataframe = self._get_dataframe(reviews_csv_filepath)

    def _get_dataframe(self, csv_filepath):
        '''
        Converts the given CSV file to a pandas DataFrame.
        '''
        with open(csv_filepath) as csv_file:
            return pd.read_csv(
                csv_file, header=None, names=FIELDNAMES,
                converters={'helpful': eval}
            )

    def extract_features(self):
        self.reviews_dataframe['helfulnessScore'] = \
            self.reviews_dataframe['helpful'].apply(compute_helpfulness_score)

    def train_model(self):
        # TODO: Use more features
        X = self.reviews_dataframe.as_matrix(['overall'])
        y = self.reviews_dataframe['helfulnessScore']

        model = svm.SVR()
        # TODO: Learn optimal kernel
        # TODO: Learn optimal parameters
        params = {'C': [0.1, 0.5]}
        grid = GridSearchCV(
            model, params, cv=5, scoring='mean_squared_error', n_jobs=-1)
        grid.fit(X, y)

        # TODO: Remove
        print()
        print(grid.best_score_)
        print('RMSE: ' + str(sqrt(abs(grid.best_score_))))

    def run_pipeline(self):
        self.extract_features()
        self.train_model()


if __name__ == '__main__':
    pass

'''
Probabilistic SVM-regression model for predicting review helpfulness
inspired by Kim et al. (2006).
'''
import time

from scipy.sparse import hstack
from sklearn.metrics.scorer import make_scorer
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import maxabs_scale
from sklearn.svm import LinearSVR

from helpfulness.data.preprocess import CV_DATA_CSV_PATH
from helpfulness.data.preprocess import DEV_DATA_CSV_PATH
from helpfulness.data.preprocess import FIELDNAMES
from helpfulness.data.relations import RELATIONS_DIRPATH
from helpfulness.data.relations import RELATION_NAMES
from helpfulness.model.evaluation import plain_pearsonr
from helpfulness.model.features import compute_helpfulness_score
from helpfulness.model.features import get_exprel_distribution
from helpfulness.model.features import get_tf_idf_matrix
from helpfulness.model.features import num_tokens

import pandas as pd


class ReviewHelpfulnessRegressionModel:

    def __init__(
            self, reviews_csv_filepath, relations_dirpath=None,
            use_discourse_relations=False):
        self.reviews_dataframe = self._get_dataframe(reviews_csv_filepath)
        print(f'Data path: "{reviews_csv_filepath}" '
              f'({len(self.reviews_dataframe)} reviews)')

        self._relations_dirpath = relations_dirpath
        self._use_discourse_relations = use_discourse_relations

        # self._model = SVR(kernel='rbf', C=1, gamma=0.001)
        self._model = LinearSVR(C=0.01, epsilon=0.1)

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

        # Add explicit discourse relations (REL)
        if self._use_discourse_relations:
            rels_df = self.reviews_dataframe['reviewID'].apply(
                get_exprel_distribution, args=[self._relations_dirpath])

            # Normalize relation frequencies
#             rels_df = rels_df.div(
#                 self.reviews_dataframe['numTokens'], axis='rows')

            self.reviews_dataframe = self.reviews_dataframe.join(rels_df)

    def get_feature_matrix(self, discourse_features_only=True):
        '''
        Returns a sparse feature matrix for the model.
        Includes standard transformation and feature scaling.
        '''
        if discourse_features_only:
            feature_columns = []
            # feature_columns = ['overall']
            feature_columns.extend(RELATION_NAMES)
            feature_matrix = self.reviews_dataframe.as_matrix(feature_columns)
            return maxabs_scale(feature_matrix)

        # Get TF-IDF-weighted document-term matrix (UGR)
        tf_idf_matrix = get_tf_idf_matrix(self.reviews_dataframe['reviewText'])

        other_feature_columns = ['overall', 'numTokens']

        if self._use_discourse_relations:
            other_feature_columns.extend(RELATION_NAMES)

        other_features_matrix = self.reviews_dataframe.as_matrix(
            other_feature_columns)

        feature_matrix = hstack([tf_idf_matrix, other_features_matrix])

        # TODO: Remove?
        # Apply logarithmic transformation to each feature measurement
        # Omitting this as it doesn't seem to have an effect
        # feature_matrix.data = apply_log_transformation(feature_matrix.data)

        # Scale each feature to the [-1, 1] range
        feature_matrix = maxabs_scale(feature_matrix)

        return feature_matrix

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
        param_grid = [
            {
                'epsilon': [0, 0.01, 0.1, 0.5, 1],
                'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000]
            }
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
        # Note: 95% confidence bounds are calculated using 10-fold CV
        print("CV Pearson r: %0.3f (± %0.3f)" % (
            scores.mean(), scores.std() * 2))

    def get_feature_weights(self):
        '''
        Performs 10-fold cross-validation and outputs the learned
        coefficients of the discourse-relation features.
        '''
        X = self.get_feature_matrix()
        y = self.get_target_vector()
        n_splits = 10
        kf = KFold(n_splits=n_splits, shuffle=True, random_state=4)
        kf.get_n_splits(X)

        dr_coef_matrix = pd.DataFrame(
            index=range(n_splits), columns=RELATION_NAMES)

        for run, (train, test) in enumerate(kf.split(X)):
            self._model.fit(X[train], y[train]).score(X[test], y[test])
            dr_coef_matrix.iloc[run] = pd.Series(
                self._model.coef_[-len(RELATION_NAMES):], index=RELATION_NAMES)

        print()
        print(dr_coef_matrix.mean().sort_values(ascending=False).round(3))


def run_experiment(use_dev_data=True, use_discourse_relations=False):
    print('--- Starting experiment ---', end='\n\n')
    start_time = time.time()

    if use_dev_data:
        reviews_csv_filepath = DEV_DATA_CSV_PATH
    else:
        reviews_csv_filepath = CV_DATA_CSV_PATH

    helpfulness_model = ReviewHelpfulnessRegressionModel(
        reviews_csv_filepath,
        relations_dirpath=RELATIONS_DIRPATH,
        use_discourse_relations=use_discourse_relations
    )

    helpfulness_model.extract_features()

    # Tune hyperparameters (only on development set!)
    # helpfulness_model.tune_hyperparams()

    helpfulness_model.get_feature_weights()

    # helpfulness_model.evaluate_model()

    print()
    print("--- Took %0.2f seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    run_experiment(use_dev_data=False, use_discourse_relations=True)

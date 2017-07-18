import pytest

from helpfulness.data.preprocess import DEV_DATA_CSV_PATH
from helpfulness.data.relations import RELATIONS_DIRPATH
from helpfulness.data.relations import RELATION_NAMES
from helpfulness.model.regression import ReviewHelpfulnessRegressionModel

import pandas as pd


@pytest.fixture
def helpfulness_model():
    return ReviewHelpfulnessRegressionModel(
        DEV_DATA_CSV_PATH,
        relations_dirpath=RELATIONS_DIRPATH
    )


class TestReviewHelpfulnessRegressionModel:

    def test__get_dataframe(self, helpfulness_model):
        # Make sure the dataframe has the right dimensions
        assert helpfulness_model.reviews_dataframe.shape == (2000, 10)

        # Make sure list conversion for helpfulness votes works
        assert type(helpfulness_model.reviews_dataframe['helpful'][1]) == list

    def test_get_feature_matrix(self, helpfulness_model):
        helpfulness_model.extract_features()
        feature_matrix = helpfulness_model.get_feature_matrix()

        # Make sure TF-IDF columns have been added to the feature matrix
        assert feature_matrix.shape == (2000, 6197)

    def test_get_feature_matrix_use_discourse_relations(
            self, helpfulness_model):
        helpfulness_model._use_discourse_relations = True
        helpfulness_model.extract_features()
        feature_matrix = helpfulness_model.get_feature_matrix()

        # Make sure discourse-relations columns  have been added
        assert feature_matrix.shape == (2000, 6212)

    def test_extract_features(self, helpfulness_model):
        helpfulness_model.extract_features()

        # Make sure an extra column for helpfulness scores has been added
        assert helpfulness_model.reviews_dataframe.shape == (2000, 12)

        assert round(helpfulness_model.reviews_dataframe[
            'helpfulnessScore'][1], 6) == 0.454545

        assert helpfulness_model.reviews_dataframe['numTokens'][1] == 327

    def test_extract_features_use_discourse_relations(self, helpfulness_model):
        helpfulness_model._use_discourse_relations = True
        helpfulness_model.extract_features()

        # Make sure extra columns for discourse relations have been added
        assert helpfulness_model.reviews_dataframe.shape == (2000, 27)

        assert helpfulness_model.reviews_dataframe.loc[
            1][RELATION_NAMES].equals(
            pd.Series(
                {
                    'Comparison.Concession': 0,
                    'Comparison.Contrast': 3,
                    'Comparison.Pragmatic concession': 0,
                    'Comparison.Pragmatic contrast': 0,
                    'Contingency.Cause': 2,
                    'Contingency.Condition': 2,
                    'Contingency.Pragmatic condition': 0,
                    'Expansion.Alternative': 1,
                    'Expansion.Conjunction': 1,
                    'Expansion.Exception': 0,
                    'Expansion.Instantiation': 0,
                    'Expansion.List': 0,
                    'Expansion.Restatement': 0,
                    'Temporal.Asynchronous': 1,
                    'Temporal.Synchrony': 1
                }, dtype=object
            )
        )

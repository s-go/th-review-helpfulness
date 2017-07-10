import pytest

from helpfulness.model.regression import ReviewHelpfulnessRegressionModel


@pytest.fixture
def helpfulness_model():
    return ReviewHelpfulnessRegressionModel('data/reviews_dev.csv')


class TestReviewHelpfulnessRegressionModel:

    def test__get_dataframe(self, helpfulness_model):
        # Make sure the dataframe has the right dimensions
        assert helpfulness_model.reviews_dataframe.shape == (2000, 10)

        # Make sure list conversion for helpfulness votes works
        assert type(helpfulness_model.reviews_dataframe['helpful'][1]) == list

    def test_extract_features(self, helpfulness_model):
        helpfulness_model.extract_features()

        # Make sure an extra column for helpfulness scores has been added
        assert helpfulness_model.reviews_dataframe.shape == (2000, 11)

        assert round(helpfulness_model.reviews_dataframe[
            'helfulnessScore'][1], 6) == 0.454545

    def test_run_pipeline(self, helpfulness_model):
        helpfulness_model.run_pipeline()

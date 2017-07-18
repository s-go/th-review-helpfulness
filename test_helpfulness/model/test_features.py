from helpfulness.model.features import compute_helpfulness_score
from helpfulness.model.features import get_exprel_distribution
from helpfulness.model.features import num_tokens

import pandas as pd


class TestFeatures:

    def test_compute_helpfulness_score(self):
        assert compute_helpfulness_score([1, 4]) == 0.25
        assert compute_helpfulness_score([0, 4]) == 0
        assert compute_helpfulness_score([4, 4]) == 1

    def test_get_exprel_distribution(self):
        relation_vector = get_exprel_distribution(
            '0e15f76e', 'test_helpfulness/fixtures')

        assert relation_vector.equals(
            pd.Series(
                {
                    'Comparison.Concession': 0,
                    'Comparison.Contrast': 13,
                    'Comparison.Pragmatic concession': 0,
                    'Comparison.Pragmatic contrast': 0,
                    'Contingency.Cause': 8,
                    'Contingency.Condition': 2,
                    'Contingency.Pragmatic condition': 0,
                    'Expansion.Alternative': 0,
                    'Expansion.Conjunction': 17,
                    'Expansion.Exception': 0,
                    'Expansion.Instantiation': 0,
                    'Expansion.List': 0,
                    'Expansion.Restatement': 0,
                    'Temporal.Asynchronous': 8,
                    'Temporal.Synchrony': 6
                }
            )
        )

    def test_get_exprel_distribution_missing_file(self):
        relation_vector = get_exprel_distribution(
            'missing', 'test_helpfulness/fixtures')

        assert relation_vector.equals(
            pd.Series(
                {
                    'Comparison.Concession': 0,
                    'Comparison.Contrast': 0,
                    'Comparison.Pragmatic concession': 0,
                    'Comparison.Pragmatic contrast': 0,
                    'Contingency.Cause': 0,
                    'Contingency.Condition': 0,
                    'Contingency.Pragmatic condition': 0,
                    'Expansion.Alternative': 0,
                    'Expansion.Conjunction': 0,
                    'Expansion.Exception': 0,
                    'Expansion.Instantiation': 0,
                    'Expansion.List': 0,
                    'Expansion.Restatement': 0,
                    'Temporal.Asynchronous': 0,
                    'Temporal.Synchrony': 0
                }
            )
        )

        # TODO: Check applying function to data frame

    def test_num_tokens(self):
        text = '''Update: Changed rating to 4 stars instead of 5, Original
        review remain below, So why i did that? it's because the video
        capture "audio" quality... they offer a fix/upgrade according to them
        here : [...](Original review)
        '''
        assert num_tokens(text) == 32

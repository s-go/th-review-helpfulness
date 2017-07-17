from helpfulness.model.features import compute_helpfulness_score
from helpfulness.model.features import num_tokens


class TestFeatures:

    def test_compute_helpfulness_score(self):
        assert compute_helpfulness_score([1, 4]) == 0.25
        assert compute_helpfulness_score([0, 4]) == 0
        assert compute_helpfulness_score([4, 4]) == 1

    def test_num_tokens(self):
        text = '''Update: Changed rating to 4 stars instead of 5, Original
        review remain below, So why i did that? it's because the video
        capture "audio" quality... they offer a fix/upgrade according to them
        here : [...](Original review)
        '''
        assert num_tokens(text) == 49

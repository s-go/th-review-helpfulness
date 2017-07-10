from helpfulness.model.features import compute_helpfulness_score


class TestFeatures:

    def test_compute_helpfulness_score(self):
        assert compute_helpfulness_score([1, 4]) == 0.25
        assert compute_helpfulness_score([0, 4]) == 0
        assert compute_helpfulness_score([4, 4]) == 1

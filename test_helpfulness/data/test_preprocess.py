from helpfulness.data.preprocess import amend_sentence_boundaries


class TestPreprocess:

    def test_amend_sentence_boundaries(self):
        text = '''That's it.A real home run? Not quite... This whole
        e-reader thing is bravo-sierra at this point.  Just wish I had
        known this before...That's my $0.02...
        '''

        target = '''That's it. A real home run? Not quite. This whole
        e-reader thing is bravo-sierra at this point.  Just wish I had
        known this before. That's my $0.02.
        '''

        assert amend_sentence_boundaries(text) == target

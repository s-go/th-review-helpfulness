from helpfulness.data.preprocess import amend_sentence_boundaries


class TestPreprocess:

    def test_amend_sentence_boundaries(self):
        text = '''That's a win-win.This whole e-reader thing is bravo-sierra
        at this point.That's my $0.02.  Just wish I had known this before...
        '''

        target = '''That's a win-win. This whole e-reader thing is bravo-sierra
        at this point. That's my $0.02.  Just wish I had known this before...
        '''

        assert amend_sentence_boundaries(text) == target

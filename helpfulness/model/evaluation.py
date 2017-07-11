'''
Metrics for evaluating regression models.
'''
from scipy.stats.stats import pearsonr


def plain_pearsonr(x, y):
    '''
    Calculates the Pearson correlation coefficient without additionally
    returning the p-value for testing non-correlation (for use as a
    scikit-learn scoring metric).
    '''
    return pearsonr(x, y)[0]

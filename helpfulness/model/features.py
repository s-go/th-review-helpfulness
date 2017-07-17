'''
Feature-extraction functions for predicting review helpfulness.
'''
from nltk import word_tokenize
from numpy import log
from sklearn.feature_extraction.text import TfidfVectorizer


def apply_log_transformation(value):
    return log(value + 1)


def compute_helpfulness_score(helpfulness_votes):
    positive_votes, total_votes = helpfulness_votes
    helpfulness_score = ((1.0 * positive_votes) / (1.0 * total_votes))
    return helpfulness_score


def num_tokens(text):
    '''
    Returns the number of tokens in the given text.
    '''
    # TODO: Use sklearn tokenizer?
    # http://scikit-learn.org/stable/modules/feature_extraction.html#common-vectorizer-usage
    return len(word_tokenize(text))


def get_tf_idf_matrix(reviews):
    '''
    Returns a sparse TF-IDF-weighted document-term matrix.

    from https://github.com/ankeshanand/review-helpfulness/blob/master/
    models/SVM/extract_features.py
    '''
    vectorizer = TfidfVectorizer(min_df=4, stop_words='english')
    return vectorizer.fit_transform(reviews)

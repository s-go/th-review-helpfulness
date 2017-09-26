'''
Feature-extraction functions for predicting review helpfulness.
'''
import os
import re

from numpy import log
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

from helpfulness.data.relations import RELATION_NAMES
from helpfulness.data.relations import match_relation_name
import pandas as pd


PRAGMATIC_TYPE_PATTERN = re.compile(r'Pragmatic c')


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
    analyze = CountVectorizer().build_analyzer()
    return len(analyze(text))


def get_exprel_distribution(filename, rel_basepath, file_ext='txt.exp.res'):
    '''
    Returns the existence of explicitly expressed discourse-relation
    types in the specified file as a 0/1-valued vector.

    :param filename: bare file name without extension
    :param rel_basepath: path to the directory containing the output of
        the PDTB-styled end-to-end discourse parser (Lin et al. 2014)
    :param file_ext: filename extension of explicit-relation files

    :rtype: pd.Series
    '''
    relation_vector = pd.Series(0, index=RELATION_NAMES)

    filepath = os.path.join(rel_basepath, f'{filename}.{file_ext}')

    if os.path.exists(filepath):
        with open(filepath) as txt_file:
            for line in txt_file:
                relation_name = match_relation_name(line)
                # Merge pragmatic types
                relation_name = PRAGMATIC_TYPE_PATTERN.sub('C', relation_name)
                try:
                    relation_vector[relation_name] = 1
                except KeyError:
                    print(
                        f'Warning: Undefined relation name "{relation_name}"')
    else:
        print(f'Error: Missing relations file "{filepath}"')

    return relation_vector


def get_tf_idf_matrix(reviews):
    '''
    Returns a sparse TF-IDF-weighted document-term matrix.

    from https://github.com/ankeshanand/review-helpfulness/blob/master/
    models/SVM/extract_features.py
    '''
    vectorizer = TfidfVectorizer(min_df=4, stop_words='english')
    return vectorizer.fit_transform(reviews)

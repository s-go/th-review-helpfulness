'''
Feature-extraction functions for predicting review helpfulness.
'''


def compute_helpfulness_score(helpfulness_votes):
    positive_votes, total_votes = helpfulness_votes
    helpfulness_score = ((1.0 * positive_votes) / (1.0 * total_votes))
    return helpfulness_score

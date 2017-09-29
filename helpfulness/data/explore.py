'''
Functions that can be used for data exploration.
'''
from helpfulness.data.preprocess import CV_DATA_CSV_PATH
from helpfulness.data.preprocess import DEV_DATA_CSV_PATH
from helpfulness.data.preprocess import FIELDNAMES
from helpfulness.data.preprocess import parse
from helpfulness.data.preprocess import to_pretty_json
from helpfulness.data.relations import RELATIONS_DIRPATH
from helpfulness.data.relations import RELATION_NAMES
from helpfulness.model.features import compute_helpfulness_score
from helpfulness.model.features import get_exprel_distribution
from helpfulness.model.features import mean_sentence_length
from helpfulness.model.features import num_tokens
import pandas as pd


def explore_reviews(csv_filepath):
    '''
    Converts the given CSV file into a pandas ``DataFrame``.
    '''
    with open(csv_filepath) as csv_file:
        reviews_df = pd.read_csv(
            csv_file, header=None, names=FIELDNAMES,
            converters={'helpful': eval}
        )

    print('Extracting features from raw data...')
    # Add number of tokens (LEN)
    reviews_df['numTokens'] = reviews_df['reviewText'].apply(num_tokens)
    reviews_df['meanSentenceLength'] = reviews_df['reviewText'].apply(
        mean_sentence_length)

    # Add helpfulness score (STR)
    reviews_df['helpfulnessScore'] = reviews_df['helpful'].apply(
        compute_helpfulness_score)

    # Add explicit discourse-relation features
    rels_df = reviews_df['reviewID'].apply(
        get_exprel_distribution, args=[RELATIONS_DIRPATH],
        count_instances=True)

    reviews_df = reviews_df.join(rels_df)

    # Calculate instances of discourse relations per hundred tokens (iph)
    reviews_df['numRelations'] = reviews_df[
        RELATION_NAMES].sum(axis=1).divide(
            reviews_df['numTokens']).multiply(100)

    reviews_without_conj_df = reviews_df.loc[
        reviews_df['Expansion.Conjunction'] == 0]

    reviews_with_conj_df = reviews_df.loc[
        reviews_df['Expansion.Conjunction'] != 0]

    print('\n--- Reviews with Expansion.Conjunction ---\n')

    print('Average number of tokens: %s' %
          reviews_with_conj_df['numTokens'].mean())

    print('Average sentence length: %s' %
          reviews_with_conj_df['meanSentenceLength'].mean())

    print('Average number of discourse relations per hundred tokens: %s' %
          reviews_with_conj_df['numRelations'].mean())

    print('Average helpfulness score: %s' %
          reviews_with_conj_df['helpfulnessScore'].mean())

    print('\n--- Reviews without Expansion.Conjunction ---\n')

    print('Average number of tokens: %s' %
          reviews_without_conj_df['numTokens'].mean())

    print('Average sentence length: %s' %
          reviews_without_conj_df['meanSentenceLength'].mean())

    print('Average number of discourse relations per hundred tokens: %s' %
          reviews_without_conj_df['numRelations'].mean())

    print('Average helpfulness score: %s' %
          reviews_without_conj_df['helpfulnessScore'].mean())


def show_helpful_example():
    for review in parse('data/reviews_Electronics_5.json.gz'):
        if review['asin'] == 'B000W9OJVA':
            print(to_pretty_json(review))


if __name__ == '__main__':
    explore_reviews(CV_DATA_CSV_PATH)

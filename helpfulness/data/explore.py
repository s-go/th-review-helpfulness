'''
Functions that can be used for data exploration.
'''
from helpfulness.data.preprocess import DEV_DATA_CSV_PATH
from helpfulness.data.preprocess import FIELDNAMES
from helpfulness.data.preprocess import parse
from helpfulness.data.preprocess import to_pretty_json
from helpfulness.model.features import compute_helpfulness_score
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

    # Add helpfulness score (STR)
    reviews_df['helpfulnessScore'] = reviews_df['helpful'].apply(
        compute_helpfulness_score)

    print(reviews_df.sort_values(['helpfulnessScore']))


def show_helpful_example():
    for review in parse('data/reviews_Electronics_5.json.gz'):
        if review['asin'] == 'B000W9OJVA':
            print(to_pretty_json(review))


if __name__ == '__main__':
    explore_reviews(DEV_DATA_CSV_PATH)
    show_helpful_example()

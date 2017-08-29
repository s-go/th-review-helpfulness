'''
Preprocess Amazon-review data obtained from He & McAuley (2016).
http://jmcauley.ucsd.edu/data/amazon/

1. Assign a unique ID to every review
2. Amend sentence boundaries to facilitate parsing
3. Filter out uninformative reviews
    * Remove reviews with less than 10 helpfulness votes
    * Remove reviews with less than 20 characters
4. Extract randomly sampled reviews (``SAMPLE_SIZE``)
5. Segment sampled reviews into development and training/test sections
   (``DEV_SIZE``)
6. Export reviews as CSV files, review texts as individual text files,
   and review IDs as one text file per section.
'''

import csv
import gzip
import hashlib
import json
import os
import random
import re


FIELDNAMES = (
    'reviewID',
    'asin',
    'helpful',
    'overall',
    'reviewText',
    'reviewTime',
    'reviewerID',
    'reviewerName',
    'summary',
    'unixReviewTime',
)

SAMPLE_SIZE = 20000
DEV_SIZE = 2000

DATA_BASE_DIR = 'data/books/'
RAW_DATA_FILENAME = 'reviews_Books_5.json.gz'

DEV_DATA_CSV_PATH = DATA_BASE_DIR + 'reviews_dev.csv'
CV_DATA_CSV_PATH = DATA_BASE_DIR + 'reviews_traintest.csv'

FULL_STOP_PATTERN = re.compile(r'([a-zA-Z])\.([a-zA-Z])')


def amend_sentence_boundaries(text):
    '''
    Returns a version of the given text with amended sentence boundaries
    to facilitate parsing. Introduces whitespace after full stops if
    missing.
    '''
    return FULL_STOP_PATTERN.sub(r'\1. \2', text)


def convert_to_csv(review_filepath, csv_filepath, review_ids_filepath):
    written_rows = 0
    review_ids = set()

    with open(csv_filepath, 'w') as csv_file, open(
            review_ids_filepath, 'w') as review_ids_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=FIELDNAMES)

        for review in parse(review_filepath):
            if use_this_review(review):
                review_id = get_hash_value(review)
                review_ids.add(review_id)
                review['reviewID'] = review_id
                review['reviewText'] = amend_sentence_boundaries(
                    review['reviewText'])

                csv_writer.writerow(review)
                written_rows += 1

                review_ids_file.write(review_id + '\n')

    print('Wrote %s rows to "%s"' % (written_rows, csv_filepath))
    print('Wrote %s IDs to "%s"' % (written_rows, review_ids_filepath))
    return review_ids


def sample_review_ids(all_review_ids, sample_review_ids_filepath):
    with open(sample_review_ids_filepath, 'w') as sample_review_ids_file:
        for review_id in random.sample(all_review_ids, SAMPLE_SIZE):
            sample_review_ids_file.write(review_id + '\n')

    print('Wrote %s IDs to "%s"' % (SAMPLE_SIZE, sample_review_ids_filepath))


def get_set_of_lines(txt_filepath):
    '''
    :return: a set containing all lines from the given text file
    :rtype: set
    '''
    with open(txt_filepath) as txt_file:
        line_set = set([line.rstrip('\n') for line in txt_file])
    return line_set


def export_sample_reviews(
        sample_review_ids_filepath, all_csv_filepath,
        sample_csv_filepath, sample_texts_dirpath):
    # Get IDs of reviews that should be in the sample
    sample_review_ids = get_set_of_lines(sample_review_ids_filepath)

    written_rows = 0

    with open(all_csv_filepath) as all_csv_file, open(
            sample_csv_filepath, 'w') as sample_csv_file:
        csv_reader = csv.DictReader(all_csv_file, fieldnames=FIELDNAMES)
        csv_writer = csv.DictWriter(sample_csv_file, fieldnames=FIELDNAMES)
        for review in csv_reader:
            if review['reviewID'] in sample_review_ids:
                csv_writer.writerow(review)
                written_rows += 1
                write_text_file(review, sample_texts_dirpath)

    print('Wrote %s rows to "%s"' % (written_rows, sample_csv_filepath))


def export_dev_traintest_reviews(
        sample_csv_filepath, sample_ids_filepath, dev_csv_filepath,
        dev_ids_filepath, traintest_csv_filepath, traintest_ids_filepath):
    '''
    Segments the given sampled data into a dev section with ``DEV_SIZE``
    and a training/test section containing the remaining data. Exports
    the segmented reviews as CSV files and their IDs as text files.
    '''
    sample_ids = get_set_of_lines(sample_ids_filepath)
    dev_ids = random.sample(sample_ids, DEV_SIZE)

    written_dev_rows = 0
    written_traintest_rows = 0

    with open(sample_csv_filepath) as sample_csv_file, \
            open(dev_csv_filepath, 'w') as dev_csv_file, \
            open(dev_ids_filepath, 'w') as dev_ids_file, \
            open(traintest_csv_filepath, 'w') as traintest_csv_file, \
            open(traintest_ids_filepath, 'w') as traintest_ids_file:
        csv_reader = csv.DictReader(sample_csv_file, fieldnames=FIELDNAMES)
        dev_csv_writer = csv.DictWriter(dev_csv_file, fieldnames=FIELDNAMES)
        traintest_csv_writer = csv.DictWriter(
            traintest_csv_file, fieldnames=FIELDNAMES)
        for review in csv_reader:
            review_id = review['reviewID']
            if review_id in dev_ids:
                dev_csv_writer.writerow(review)
                written_dev_rows += 1
                dev_ids_file.write(review_id + '\n')
            else:
                traintest_csv_writer.writerow(review)
                written_traintest_rows += 1
                traintest_ids_file.write(review_id + '\n')

    print('Wrote %s rows to "%s"' % (written_dev_rows, dev_csv_filepath))
    print('Wrote %s rows to "%s"' % (
        written_traintest_rows, traintest_csv_filepath))


def write_text_file(review, dirpath):
    # Check for missing directories
    if not os.path.exists(dirpath):
        print('Created directory "%s".' % dirpath)
        os.makedirs(dirpath)

    filename = f"{review['reviewID']}.txt"
    filepath = os.path.join(dirpath, filename)

    with open(filepath, 'w') as fout:
        fout.write(review['reviewText'])


def get_hash_value(obj):
    """
    Returns a hash value for the given object.

    :param obj: the object to hash
    :type obj: any JSON-serializable object

    :returns: a hash value for the given object
    :rtype: int

    Notes:

        * For JSON-equivalent objects, the same ID will be returned.
        * This also works for nested dictionaries.

    See http://stackoverflow.com/questions/19851990/
    """
    value = json.dumps(
        obj, sort_keys=True, separators=(',', ':')).encode('utf-8')
    return hashlib.sha1(value).hexdigest()


def use_this_review(review):
    # Ignore reviews with less than 10 helpfulness votes
    if review['helpful'][1] < 10:
        return False

    # Ignore reviews with less than 20 characters
    if len(review['reviewText']) < 20:
        return False

    return True


def parse(path):
    g = gzip.open(path, 'r')

    for l in g:
        yield eval(l)


def to_pretty_json(obj):
    return json.dumps(obj, indent=4, separators=(',', ': '),
                      sort_keys=True, ensure_ascii=False)


if __name__ == '__main__':
    # 1. Assign unique review IDs, filter out ininformative reviews,
    #    export reviews as CSV file and review IDs as text file
    # --
    all_review_ids = convert_to_csv(
        DATA_BASE_DIR + RAW_DATA_FILENAME,
        DATA_BASE_DIR + 'all_reviews.csv',
        DATA_BASE_DIR + 'all_review_ids.txt'
    )

    # 2. Randomly sample 20,000 reviews, export their IDs as text file
    # --
    sample_review_ids(all_review_ids, DATA_BASE_DIR + 'sample_review_ids.txt')

    # 3. Export sampled reviews as CSV file and individual text files
    #    containing only the review texts
    # --
    export_sample_reviews(
        DATA_BASE_DIR + 'sample_review_ids.txt',
        DATA_BASE_DIR + 'all_reviews.csv',
        DATA_BASE_DIR + 'sample_reviews.csv',
        DATA_BASE_DIR + 'sample_reviews'
    )

    # 4. Segment sampled reviews into development and training/test sections
    # --
    export_dev_traintest_reviews(
        DATA_BASE_DIR + 'sample_reviews.csv',
        DATA_BASE_DIR + 'sample_review_ids.txt',
        DEV_DATA_CSV_PATH,
        DATA_BASE_DIR + 'dev_review_ids.txt',
        CV_DATA_CSV_PATH,
        DATA_BASE_DIR + 'cv_review_ids.txt'
    )

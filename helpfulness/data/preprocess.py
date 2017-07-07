import csv
import gzip
import hashlib
import json
import os
import random


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


def export_sample_reviews(
        sample_review_ids_filepath, all_csv_filepath,
        sample_csv_filepath, sample_texts_dirpath):
    # Get IDs of reviews that should be in the sample
    with open(sample_review_ids_filepath) as sample_review_ids_file:
        sample_review_ids = set(
            [line.rstrip('\n') for line in sample_review_ids_file])

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
        obj, sort_keys=True, separators=(',', ':')
    ).encode('utf-8')
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
    #     all_review_ids = convert_to_csv(
    #         'data/reviews_Electronics_5.json.gz',
    #         'data/reviews_Electronics_5.csv',
    #         'data/review_ids_all.txt'
    #     )

    # sample_review_ids(all_review_ids, 'data/review_ids_sample.txt')

    export_sample_reviews(
        'data/review_ids_sample.txt',
        'data/reviews_Electronics_5.csv',
        'data/reviews_sample.csv',
        'data/reviews_sample')

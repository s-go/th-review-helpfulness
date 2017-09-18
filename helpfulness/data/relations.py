'''
Functions for preprocessing discourse-relation files created by the
PDTB-styled end-to-end discourse parser (Lin et al. 2014).
'''
from glob import glob
import os
import re

from helpfulness.data.preprocess import DATA_BASE_DIR

RELATIONS_DIRPATH = DATA_BASE_DIR + 'exp_rel_output'

RELATION_NAMES = [
    'Comparison.Concession',
    'Comparison.Contrast',
    'Comparison.Pragmatic concession',
    'Comparison.Pragmatic contrast',
    'Contingency.Cause',
    'Contingency.Condition',
    'Contingency.Pragmatic condition',
    'Expansion.Alternative',
    'Expansion.Conjunction',
    'Expansion.Exception',
    'Expansion.Instantiation',
    'Expansion.List',
    'Expansion.Restatement',
    'Temporal.Asynchronous',
    'Temporal.Synchrony'
]

RELATION_PATTERN = re.compile(r'.*\|(.*)')


def match_relation_name(line):
    match = RELATION_PATTERN.match(line)
    relation_name = match.group(1)
    return relation_name


def get_relation_names(dirpath):
    relation_names = set()

    for i, f in enumerate(glob(os.path.join(dirpath, '*.exp.res'))):
        with open(f) as txt_file:
            for line in txt_file:
                relation_name = match_relation_name(line)
                # Detect level-1 relations
                if '.' not in relation_name:
                    print(f)
                    break
                relation_names.add(relation_name)

    print(f'\nExamined {i} files. Found the following relations:\n')

    for relation_name in sorted(relation_names):
        print(f"'{relation_name}',")


if __name__ == '__main__':
    get_relation_names(RELATIONS_DIRPATH)

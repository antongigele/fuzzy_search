import json
import pandas as pd
from nltk import word_tokenize
from filepath import append_path, data_source_path, path, output_path
import sys
sys.path.append(append_path)
from export_data import export_list2csv
from load_data import load_json2data

## Prepare data
def get_atoms_from_col(dataframe, col):
    dataframe[col] = dataframe[col].fillna(" ")
    topic_names = {w.lower() for w in dataframe[col].unique()}
    topic_names_atomized = set()
    for string in topic_names:
        sep_by_dot_list = string.split('.')
        for substring in sep_by_dot_list:
            topic_names_atomized.update(word_tokenize(substring))
    return topic_names, topic_names_atomized

def dissolve_subsets_into_set(input_set):
    new_set = set()
    for subset in input_set:
        new_set.update(subset.split(","))
    return {string.strip() for string in new_set}

def create_target_list():
    pass

if __name__ == "__main__":
    create_target_list()
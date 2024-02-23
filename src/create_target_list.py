import pandas as pd
from nltk import word_tokenize
from filepath import append_path, data_source_path, path, output_path
import sys
sys.path.append(append_path)

def get_single_words_from_col(dataframe, col):
    topic_names_set = set()
    for string in {w.lower() for w in dataframe[col].unique()}:
        sep_by_dot_list = string.split('.')
        for substring in sep_by_dot_list:
            topic_names_set.update(word_tokenize(substring))
    return topic_names_set

def get_sentences_from_col(dataframe, col):
    return {w.lower() for w in dataframe[col].unique()}

def dissolve_subsets_into_set(input_set):
    new_set = set()
    for subset in input_set:
        new_set.update(subset.split(","))
    return {string.strip() for string in new_set}

def create_target_list(filepath, col):
    df = pd.read_csv(filepath)
    df[col] = df[col].fillna(" ")
    

if __name__ == "__main__":
    create_target_list()
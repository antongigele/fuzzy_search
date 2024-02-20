import json
import pandas as pd
from filepath import analytics_path, append_path, data_source_path
import sys
sys.path.append(append_path)
from export_data import export_dict2json

def create_count_dict():
    two_char_words_df = pd.read_csv(analytics_path + 'two_char_words_cnt.csv')
    three_char_words_df = pd.read_csv(analytics_path + 'three_char_words_cnt.csv')
    four_char_words_df = pd.read_csv(analytics_path + 'four_char_words_cnt.csv')
    five_char_words_df = pd.read_csv(analytics_path + 'five_char_words_cnt.csv')
    six_char_words_df = pd.read_csv(analytics_path + 'six_char_words_cnt.csv')
    seven_char_words_df = pd.read_csv(analytics_path + 'seven_char_words_cnt.csv')
    eight_char_words_df = pd.read_csv(analytics_path + 'eight_char_words_cnt.csv')
    nine_char_words_df = pd.read_csv(analytics_path + 'nine_char_words_cnt.csv')
    ten_char_words_df = pd.read_csv(analytics_path + 'ten_char_words_cnt.csv')
    frames = [two_char_words_df, three_char_words_df, four_char_words_df, five_char_words_df, six_char_words_df, seven_char_words_df, eight_char_words_df, nine_char_words_df, ten_char_words_df]
    all_words_count_df = pd.concat(frames)
    all_words_count_dict = all_words_count_df[["term", "count"]].set_index('term').T.to_dict('records')[0]

    with open(f'{analytics_path}pornstars_names_occurences.json') as json_file:
        pornstars_names_dict = json.load(json_file)
    with open(f'{analytics_path}studios_names_occurences.json') as json_file:
        studios_names_dict = json.load(json_file)
    pornstars_names_dict.update(studios_names_dict)
    all_words_count_dict.update(pornstars_names_dict)

    export_dict2json(data_source_path, "all_words_count_dict.json", all_words_count_dict)

if __name__ == "__main__":
    create_count_dict()
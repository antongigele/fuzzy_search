import pandas as pd
from ordered_set import OrderedSet
import concurrent.futures
import json
from collections import Counter
from time import time
from functools import partial
import typing

path = "/Users/antongigele/Desktop/hulkshare_projects/anton-concept-node/csv_imports/"

def read_input_data(filepath: str):
    return pd.read_csv(filepath)

def create_single_words_set(queries) -> set:
    single_words_set = OrderedSet()
    for q in queries:
        single_words_set.update(set(q.split()))
        
    return single_words_set

def create_n_len_words_list(words_set: set, n: int) -> list:
    return [word for word in words_set if len(word) == n]

def get_query_occurrences(string_to_count, query_list: list) -> list:
    string_to_count_start = string_to_count + " "
    string_to_count_middle = " " + string_to_count + " "
    string_to_count_end = " " + string_to_count
    query_occurrences = []

    for query in query_list:
        if query.startswith(string_to_count_start):
            query_occurrences.append(query)
        elif string_to_count_middle in query:
            query_occurrences.append(query)
        elif query.endswith(string_to_count_end):
            query_occurrences.append(query)
    return query_occurrences

def get_most_common_used_words2single_word(word: str, most_common: int) -> tuple:
    input_df = read_input_data(path + "queries.csv")
    query_occurences_single_word = get_query_occurrences(word, list(input_df["query"]))
    word_counter = Counter(" ".join(query_occurences_single_word).split(" "))
    del word_counter[word]

    try:
        result_tuple = word_counter.most_common(most_common)[most_common-1]
    except IndexError:
        result_tuple =  ("", 0)

    return result_tuple
    

def count_occurrences(string_to_count: str, list_of_strings_str: str) -> int:
    return list_of_strings_str.count(" " + string_to_count + " ")

def create_n_char_words_dataframe(n: int, df_column: pd.Series) -> pd.DataFrame:
    single_words_set = create_single_words_set(df_column)
    list_of_query_strings_str = " ".join(df_column)

    n_char_words = create_n_len_words_list(single_words_set, n)
    n_char_words_count_dict = {word: count_occurrences(word, list_of_query_strings_str) for word in n_char_words}

    n_char_words_df = pd.DataFrame(n_char_words,
               columns =['term'])
    n_char_words_df["count"] = n_char_words_df["term"].map(n_char_words_count_dict)
    n_char_words_df = n_char_words_df.sort_values(by="count", ascending=False)

    n_char_words_df["occurs_most_with"] = [get_most_common_used_words2single_word(word, 1)[0] for word in n_char_words_df["term"]]
    n_char_words_df["occurs_second_most_with"] = [get_most_common_used_words2single_word(word, 2)[0] for word in n_char_words_df["term"]]

    return n_char_words_df

def get_strings_counts(tupel: tuple, strings_to_count: typing.Iterable[str], list_of_target_strings: list) -> dict:
    start, stop = tupel[0], tupel[1]
    print(f"{start} :", f"{stop}","subprocess")

    strings_count_list = list(strings_to_count)[start:stop]
    joined_list = " ".join(list_of_target_strings)
    zero_counts_dict = dict()
    for word in list(strings_count_list):
        if word not in joined_list:
            strings_count_list.remove(word)
            zero_counts_dict[word] = 0

    strings_count_dict = {word: count_occurrences(word, joined_list) for word in strings_count_list}
    strings_count_dict.update(zero_counts_dict)
    return strings_count_dict

def multiprocess(function, definition_set, target_set, segment_size=500):
    dataset_length=len(definition_set)
    segments_lupel_list = [[i,i+segment_size] for i in range(0, dataset_length, segment_size)]
    segments_lupel_list[-1][1] = dataset_length
    partial_generate_results = partial(function, strings_to_count=definition_set, list_of_target_strings=target_set)

    with concurrent.futures.ProcessPoolExecutor(4) as executor:
        results = executor.map(partial_generate_results, segments_lupel_list)

    all_results = {}
    for result in results:
        all_results.update(result)

    return all_results

def embedded_word_occurences2dict(word_list: typing.Iterable[str], dataframe: pd.DataFrame, col_name: str) -> dict:
    embedded_word_occurences_dict = {}
    for word in word_list:
        embedded_word_occurences_dict[word] = dataframe[dataframe[col_name].str.contains(word)]["cnt"].sum()
    return embedded_word_occurences_dict

def export_dict2json(path, filename, dict):
    with open(path + filename, "w") as outfile: 
        json.dump(dict, outfile)

if __name__ == "__main__":
    pass
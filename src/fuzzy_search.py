from Levenshtein import distance as levenshtein_distance
from src.filepath import append_path, data_source_path
import sys
sys.path.append(append_path)
from load_data import load_json2data, load_csv2list
import math
from spellcheck import pornstar_names, studios_names

## Load occurences count dict
all_words_count_dict = load_json2data(data_source_path, "all_words_count_dict.json")

## Load target list
final_target_list = load_csv2list(data_source_path, "final_target_list.csv")

space_names = list(pornstar_names) + list(studios_names)
space_names = [name for name in space_names if " " in name.strip()]

def get_closest_match(query_input, target_list, all_words_occurences_dict):
    target_list = [w.lower() for w in target_list]
    query_input = query_input.lower()

    query_input_list = query_input.split()
    answer_list = []
    for string in query_input_list:
        query_input = query_input.strip()
        if (not string in target_list):  
            distance_dict = {}
            for name in target_list:
                distance_dict[name] = levenshtein_distance(string, name)
            minimum_value = min(distance_dict.values())
            minimum_keys = [key for key in distance_dict if distance_dict[key]==minimum_value]
            words_weight_dict = {}
            for word in minimum_keys:
                try:
                    words_weight_dict[word] = all_words_occurences_dict[word]
                except KeyError:
                    words_weight_dict[word] = 0
            max_key = max(words_weight_dict, key=words_weight_dict.get)
            
            answer_list.append(max_key)

        else:
            answer_list.append(string)

    return " ".join(answer_list)

def get_closest_match1space(query_input, target_list, all_words_occurences_dict):
    target_list = [w.lower() for w in target_list]
    query_input = query_input.lower()

    string = query_input.strip()
    if (not string in target_list):  
        distance_dict = {}
        for name in target_list:
            distance_dict[name] = levenshtein_distance(string, name)
        minimum_value = min(distance_dict.values())
        minimum_keys = [key for key in distance_dict if distance_dict[key]==minimum_value]
        words_weight_dict = {}
        for word in minimum_keys:
            try:
                words_weight_dict[word] = all_words_occurences_dict[word]
            except KeyError:
                words_weight_dict[word] = 0
        max_key = max(words_weight_dict, key=words_weight_dict.get)
            
        return max_key

    else:
        return string

### Combination of single and double names matching
def get_closest_match_combined(query_input, target_list, all_words_occurences_dict):
    if " " in query_input:
        print("space in query")
        candidate_list = [get_closest_match1space(query_input, space_names, all_words_occurences_dict)]
    else:
        single_word_output = get_closest_match(query_input, target_list, all_words_occurences_dict)
        two_words_with_space_output = get_closest_match1space(query_input, target_list, all_words_occurences_dict)
        candidate_list = [single_word_output, two_words_with_space_output]
    words_weight_dict = {}
    for word in [single_word_output, two_words_with_space_output]:
        if word not in all_words_occurences_dict:
            all_words_occurences_dict[word] = 0
        try:
            words_weight_dict[word] = all_words_occurences_dict[word]
        except KeyError:
            words_weight_dict[word] = 0
    max_key = max(words_weight_dict, key=words_weight_dict.get)
    if levenshtein_distance(query_input, max_key) > math.ceil(2*len(max_key)/3):
        max_key = query_input
    return max_key


if __name__ == "__main__":
    query_input = input("Enter query: ")

    print(get_closest_match_combined(query_input, final_target_list, all_words_count_dict))

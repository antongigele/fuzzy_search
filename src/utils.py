import json
import csv

def load_csv2list(path, filename):
    data_list = []
    with open(path + filename, 'r', newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        
        data_list = [item for sublist in csv_reader for item in sublist]

    return data_list

def load_json2data(path, filename):
    with open(path + filename) as json_file:
        return json.load(json_file)
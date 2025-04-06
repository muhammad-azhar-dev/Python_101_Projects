import json

# This function will read json file and return data as a python list
def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data

json_file_path = 'sample.json'
data = read_json_file(json_file_path)
print(data)
import json

def write_json_file(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
        print(f"Successfully added data in {file_path}")

json_file_path = 'sample.json'
data = [
    {
        "id":1,
        "name":"Ali",
        "age":"34"
    },
    {
        "id":2,
        "name":"Sameer",
        "age":"22"
    }
]
write_json_file(json_file_path, data)
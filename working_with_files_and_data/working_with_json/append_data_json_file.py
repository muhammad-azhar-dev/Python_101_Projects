import json

def append_to_json_file(file_path, new_data):

    # Read existing data
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Append new data
    data.append(new_data)

    # Write back to file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
        print(f"Successfully append data in {file_path}")


json_file_path = 'sample.json'
data =   {
        "id":3,
        "name":"Alex",
        "age":"44"
    }
append_to_json_file(json_file_path, data)
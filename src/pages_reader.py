import json

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def convert_to_array_elements(data):
    array_elements = []
    for link in data.values():
        array_elements.append(link)
    return array_elements


# file_path = 'pages.json'
def pages_reader(file_path):
    json_data = read_json_file(file_path)
    array_elements = convert_to_array_elements(json_data)
    return array_elements

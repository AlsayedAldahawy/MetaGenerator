import json
import csv
import os

# Function to read JSON files
def read_json_file(file_path):
    links = []
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        data = json.load(file)
        for row in data:
            if 'link' in row:
                links.append(row['link'])
    return links

# Function to read CSV files
def read_csv_file(file_path):
    links = []
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if 'link' in row:
                links.append(json.loads(row['link']))
    return links

# Function to convert data to array elements
# def convert_to_array_elements(data):
#     array_elements = []
#     for link in data.values():
#         array_elements.append(link)
#     return array_elements

# Function to read pages from either JSON or CSV file
def pages_reader(file_path):
    print("--------------page reader------------------")
    _, file_extension = os.path.splitext(file_path)

    if file_extension.lower() == '.json':
        data = read_json_file(file_path)
    elif file_extension.lower() == '.csv':
        data = read_csv_file(file_path)
    else:
        raise ValueError("Unsupported file format. Please provide a JSON or CSV file.")

    # array_elements = convert_to_array_elements(data)
    print("--------------page reader data------------------", data)

    return data

# Example usage
# file_path = 'pages.json' or 'pages.csv'
# pages = pages_reader(file_path)


# print(read_csv_file("../uploads/paa.csv"))

# print(read_json_file("../uploads/paa.json"))

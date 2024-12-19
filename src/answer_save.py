def save_metadescription(strings, file_name):
    """
    Save an array of strings to a text file, with each string on a new line.

    :param strings: List of strings to be saved.
    :param file_name: Name of the file where the strings will be saved.
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        for string in strings:
            file.write(string + '\n')



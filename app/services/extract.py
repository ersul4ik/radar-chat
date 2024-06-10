import yaml


def extract_data_from_file(file_path) -> dict:
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)

    return data

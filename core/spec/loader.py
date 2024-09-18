import json

def read_class_from_json(json_file_path):
    # Read the JSON file
    with open(json_file_path, 'r') as file:
        class_spec = json.load(file)

    # Extract class information
    class_name = class_spec['ClassName']
    properties = class_spec['Properties']
    return class_spec
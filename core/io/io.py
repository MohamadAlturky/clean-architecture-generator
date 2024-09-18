
import os
import json

def read_json_files_in_folder(folder_path):
    json_contents = []
    
    # Check if the folder exists
    if not os.path.isdir(folder_path):
        print(f"Error: The folder {folder_path} does not exist.")
        return json_contents

    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Check if it's a file and has a .json extension
        if os.path.isfile(file_path) and filename.lower().endswith('.json'):
            try:
                # Open and read the JSON file
                with open(file_path, 'r', encoding='utf-8') as file:
                    json_content = json.load(file)
                    json_contents.append(json_content)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON in {filename}: {str(e)}")
            except Exception as e:
                print(f"Error reading {filename}: {str(e)}")

    return json_contents



def write_to_file(file_name, content, mode='w'):
    with open(file_name, mode) as file:
        file.write(content)

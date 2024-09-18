# from core.spec.loader import read_class_from_json
# from core.build.property import build_property
# from core.build.classes import build_data_class
# spec = read_class_from_json("person.json")
# namespace = "Donut.DTOs"
# usings = """
# using System.text;
# """
# properties = ""
# for i in spec["Properties"]:
#     properties = properties + build_property(i["Name"],i["Type"]) + "\n"
    
# print(build_data_class(spec["ClassName"]+"DTO",properties,namespace,usings))
from core.build.mappers import build_mapper
from core.io.io import read_json_files_in_folder,write_to_file
from core.build.dto import build_dto, build_request
from core.build.repository import build_repository
folder_path = "./spec"
json_files = read_json_files_in_folder(folder_path)

print(f"\nTotal JSON files read: {len(json_files)}")

for content in json_files:
    # print(build_dto(content))
    # print("--------")
    # print(build_request("Create",content))
    # print("--------")
    # print(build_request("Update",content))
    # print(build_mapper(content))
    # print("--------")
    class_name = content["ClassName"]
    write_to_file(f"./dist/{class_name}.cs",build_repository(content))
    
    
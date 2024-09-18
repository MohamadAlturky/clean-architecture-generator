from core.build.property import build_property
from core.build.classes import build_data_class

def build_dto(spec):
    namespace = "Donut.DTOs"
    usings = """
using System.text;
"""
    properties = ""
    for i in spec["Properties"]:
        properties = properties + build_property(i["Name"],i["Type"]) + "\n"
        
    return build_data_class(spec["ClassName"]+"DTO",properties,namespace,usings)


def build_request(perfix, spec):
    namespace = "Donut.Requests"
    usings = """
using System.text;
"""
    properties = ""
    for i in spec["Properties"]:
        properties = properties + build_property(i["Name"],i["Type"]) + "\n"
        
    return build_data_class(perfix+spec["ClassName"]+"Request",properties,namespace,usings)

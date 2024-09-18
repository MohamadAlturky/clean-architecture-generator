def build_mapper( spec):
    namespace = "Donut.Mappers"
    usings = """
using System.text;
"""
    entity_name = spec["ClassName"]
    name = f"{entity_name}Mapper"
    properties = ""
    for i in spec["Properties"]:
        property = i["Name"]
        properties = properties + f"""
                {property} = request.{property},
        """
        
    return f"""
    {usings}
    namespace {namespace};

    public class {name} 
    {{ 
        public {entity_name} Map(Create{entity_name}Request request)
        {{
            return new {entity_name}()
            {{
              {properties}  
            }};
        }}
        public {entity_name} Map(Update{entity_name}Request request)
        {{
            return new {entity_name}()
            {{
              {properties}  
            }};
        }}
    }}
    """
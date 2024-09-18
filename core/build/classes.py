def build_data_class(name,properties,namespace,usings):
    return f"""
{usings}
namespace {namespace};

public class {name} 
{{ 
{properties}
}}
"""
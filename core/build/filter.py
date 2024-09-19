def represent(name, type):
    s = f"""
    // name property
    public {type} {name}Equals {{ get; set; }}
    public {type} {name}NotEqual {{ get; set; }}
    public bool Select{name} {{ get; set; }}
    public bool OrderBy{name}Ascending {{ get; set; }}
    public bool OrderBy{name}Descending {{ get; set; }}
    """
    if type == "string":
        s = s + f"""
    public {type} {name}Contains {{ get; set; }}
    public {type} {name}StartsWith {{ get; set; }}
    public {type} {name}EndsWith {{ get; set; }}
        """
    if type in ["int", "decimal", "double", "long"]:
        s += f"""
    public {type} {name}LessThanNumber {{ get; set; }}
    public {type} {name}BiggerThanNumber {{ get; set; }}
    public {type} {name}LessThanOrEqualNumber {{ get; set; }}
    public {type} {name}BiggerThanOrEqualNumber {{ get; set; }}
        """

    # Check for date types
    if type in ["DateTime", "DateOnly"]:
        s += f"""
    public {type} {name}LessThanDate {{ get; set; }}
    public {type} {name}BiggerThanDate {{ get; set; }}
    public {type} {name}LessThanOrEqualDate {{ get; set; }}
    public {type} {name}BiggerThanOrEqualDate {{ get; set; }}
        """
        
    return s

def build_filter_class(name,properties):
    props = ''
    for i in properties:
        props += represent(i["Name"],i["Type"])
    return f"""
using Donut.Core.Pagination;
using Donut.Core.Filter;

namespace Donut.Filters;

public class {name}Filter : IFilter
{{ 
    // For Every Filter
    public PaginatedRequest PaginatedRequest {{ get; set; }}
    public bool EagerLoading {{ get; set; }} = true;
        
    {props}
}}
"""
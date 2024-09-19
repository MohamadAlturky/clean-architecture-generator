
def build_filter_executor_class(name,properties):
  
    return f"""
using Donut.Core.Filter;
using Donut.QueryBuilding.Execution;
using Microsoft.Data.SqlClient;
using System.Text;
using Donut.Core.Pagination;

namespace Donut.Filter.Execution;

public interface I{name}FilterExecutor: IFilterExecutor<{name}, {name}Filter> {{}}

public class {name}FilterExecutor: I{name}FilterExecutor
{{
    private readonly QueryExecutor _executor;

    public {name}FilterExecutor(QueryExecutor executor)
    {{
        _executor = executor;
    }}
    
    public PaginatedResponse<{name}> Execute({name}Filter filter)        
    {{
        var whereQueryBuilder = new StringBuilder();
        var selectQueryBuilder = new StringBuilder();
        var orderByQueryBuilder = new StringBuilder();
        var parameters = new List<SqlParameter>();
        
         bool isFirstSelect = True;

            if (filter.EagerLoading)
            {{
                selectQueryBuilder.Append("*");
            }}
            else
            {{
                
            }}
    }}
}}
"""
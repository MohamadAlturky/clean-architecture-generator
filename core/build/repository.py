def generate_parameter_names(properties):
    # Create a list of formatted parameter names
    parameter_names = [f"{prop['Name']} = @{prop['Name']}" for prop in properties]
    
    result = ", ".join(parameter_names)
    
    return result

def get_formatted_properties(properties):

    # Exclude the property named "Id"
    properties = [prop["Name"] for prop in properties if prop["Name"] != "Id"]
    
    # Create the formatted strings
    property_names = ", ".join([f"[{prop}]" for prop in properties])
    parameter_names = ", ".join([f"@{prop}" for prop in properties])
    
    return property_names, parameter_names


def build_delete_function(class_name, properties):
    return f"""
    public async Task Delete({class_name} entity)
    {{
        using (var connection = _factory.CreateConnection())
        {{
            var sql = "DELETE FROM {class_name} WHERE Id = @Id;"
            await connection.ExecuteAsync(sql, entity);
        }}
    }}
    public async Task DeleteTransactional({class_name} entity, IDbConnection connection, IDbTransaction transaction)
    {{
        var sql = "DELETE FROM {class_name} WHERE Id = @Id;"
        await connection.ExecuteAsync(sql, entity, transaction);
    }}
"""
def build_update_function(class_name, properties):
    return f"""
    public async Task Update({class_name} entity)
    {{
        using (var connection = _factory.CreateConnection())
        {{
            var sql = "UPDATE {class_name} SET {generate_parameter_names(properties)} WHERE Id = @Id;"
            await connection.ExecuteAsync(sql, entity);
        }}
    }}
    
    public async Task UpdateTransactional({class_name} entity, IDbConnection connection, IDbTransaction transaction)
    {{
        var sql = "UPDATE {class_name} SET {generate_parameter_names(properties)} WHERE Id = @Id;"
        await connection.ExecuteAsync(sql, entity, transaction);
    }}
"""
def build_add_function(class_name, properties):
    property_names, parameter_names=get_formatted_properties(properties)
    return f"""
    public async Task<{class_name}> Add({class_name} entity)
    {{
        using (var connection = _factory.CreateConnection())
        {{
            var sql = "INSERT INTO {class_name} ({property_names}) VALUES ({parameter_names}); SELECT CAST(SCOPE_IDENTITY() AS int);"
            var id = await connection.ExecuteScalarAsync<int>(sql, entity);
            entity.Id = id; 
            return entity;
        }}
    }}
    public async Task<{class_name}> AddTransactional({class_name} entity, IDbConnection connection, IDbTransaction transaction)
    {{
        var sql = "INSERT INTO {class_name} ({property_names}) VALUES ({parameter_names}); SELECT CAST(SCOPE_IDENTITY() AS int);"
        var id = connection.ExecuteScalarAsync<int>(sql, entity, transaction);
        entity.Id = id; 
        return entity;
    }}
"""

def build_repository(spec):
    namespace = "Donut.Mappers"
    entity_name = spec["ClassName"]
    className = f"{entity_name}Repository"
    add = build_add_function(entity_name,spec["Properties"])    
    update = build_update_function(entity_name,spec["Properties"])    
    delete = build_delete_function(entity_name,spec["Properties"])    
    return f"""
using System.Data;
using Dapper;
using Donut.Core.DatabaseConnection;
using Donut.Core.Repositories;
using Donut.Core.Tabels;

namespace {namespace};
public interface I{className}: IRepository<{entity_name}> {{ }}

public class {className}: I{className}
{{
    private readonly IDbConnectionFactory _factory;
    public {className}(IDbConnectionFactory factory)
    {{
        _factory=factory;
    }}
    {add}
    {update}
    {delete}
}}

"""
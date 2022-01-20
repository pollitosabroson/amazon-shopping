import os

from ariadne import (
    ObjectType, load_schema_from_path, make_executable_schema,
    snake_case_fallback_resolvers
)

PATH = os.path.dirname(os.path.abspath(__file__))
query = ObjectType("Query")

type_defs = load_schema_from_path(f'{PATH}/schema.graphql')


schema = make_executable_schema(
    type_defs, query,
    snake_case_fallback_resolvers
)
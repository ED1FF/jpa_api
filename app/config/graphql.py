
import strawberry
from strawberry.fastapi import GraphQLRouter

@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"

schema = strawberry.Schema(Query)
graphql_app = GraphQLRouter(schema)

def init_graphql(app):
  app.include_router(graphql_app, prefix="/graphql")

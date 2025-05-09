import strawberry

from strawberry.fastapi import GraphQLRouter
from app.api.mutations import Mutation
from app.api.queries import Query

schema = strawberry.Schema(query = Query, mutation = Mutation)
graphql_app = GraphQLRouter(schema)

def init_graphql(app):
  app.include_router(graphql_app, prefix="/graphql")

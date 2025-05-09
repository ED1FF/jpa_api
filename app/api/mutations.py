import strawberry

from app.models import UserType
from app.api.resolvers import user as user_resolvers

@strawberry.type
class Mutation:
    create_user: UserType = strawberry.field(resolver=user_resolvers.create_user)

import strawberry

from typing import List, Optional
from app.models import UserType
from app.api.resolvers import user as user_resolvers

@strawberry.type
class Query:
    user: Optional[UserType] = strawberry.field(resolver=user_resolvers.get_user_by_id)
    users: List[UserType] = strawberry.field(resolver=user_resolvers.get_all_users)

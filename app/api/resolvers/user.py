from app.models import User, UserType
from typing import List

def to_user_type(user: User) -> UserType:
    return UserType(
        id=str(user.id),
        username=user.username,
        email=user.email,
        created_at=str(user.created_at),
        updated_at=str(user.updated_at),
    )

# Queries
async def get_user_by_id(user_id: str) -> UserType:
    user = await User.get(id=user_id)
    return to_user_type(user)

async def get_all_users() -> List[UserType]:
    users = await User.all()
    return [to_user_type(user) for user in users]

# Mutations
async def create_user(username: str, email: str, password: str) -> UserType:
    user = await User.create(username=username, email=email, password=password)
    return to_user_type(user)


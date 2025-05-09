import uuid
import strawberry
from tortoise import fields
from tortoise.models import Model

@strawberry.type
class UserType:
    id: str
    username: str
    email: str
    created_at: str
    updated_at: str

class User(Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4, index=True)
    username = fields.CharField(max_length=50, unique=True, index=True)
    email = fields.CharField(max_length=254, unique=True, index=True)
    password = fields.CharField(max_length=128)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "users"

import uuid
from tortoise import fields
from tortoise.models import Model

class User(Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)
    username = fields.CharField(max_length=50, unique=True)
    email = fields.CharField(max_length=50, unique=True)

    class Meta:
        table = "users"

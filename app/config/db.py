from tortoise.contrib.fastapi import register_tortoise
from app.config.settings import Settings


TORTOISE_ORM = {
    "connections": {
        "default": Settings().database_url,
    },
    "apps": {
        "models": {
            "models": ["app.models", "aerich.models"],
            "default_connection": "default",
        }
    },
}

def init_db(app):
    register_tortoise(
        app,
        config=TORTOISE_ORM,
        generate_schemas=False,
        add_exception_handlers=True,
    )

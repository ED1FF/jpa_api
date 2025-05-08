from tortoise.contrib.fastapi import register_tortoise


TORTOISE_ORM = {
    "connections": {
        "default": "postgres://postgres:postgres@db:5432/jpa_development",
    },
    "apps": {
        "models": {
            "models": ["app.models", "aerich.models"],  # Add aerich.models here
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

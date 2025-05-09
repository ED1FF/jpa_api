from tortoise.contrib.fastapi import register_tortoise


TORTOISE_ORM = {
    "connections": {
        "default": "postgres://postgres:postgres@db:5432/jpa_development", # TODO: Use ENV
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

from typing import Union
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Register Tortoise ORM with PostgreSQL
register_tortoise(
    app,
    db_url="postgres://postgres:postgres@db:5432/jpa_development",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

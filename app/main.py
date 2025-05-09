from fastapi import FastAPI

from app.config.db import init_db
from app.config.graphql import init_graphql

app = FastAPI()

init_db(app)
init_graphql(app)

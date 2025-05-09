from fastapi import FastAPI

from app.config.db import init_db
from app.config.graphql import init_graphql

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Worldd"}

init_db(app)
init_graphql(app)

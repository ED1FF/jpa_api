from fastapi import FastAPI

from app.config.db import init_db

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Worldd"}

init_db(app)

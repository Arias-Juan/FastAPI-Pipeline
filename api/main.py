from fastapi import FastAPI
from load_psql import load_api

app = FastAPI()

app.include_router(load_api)

@app.get('/')
async def root():
    return {"Globant": "DE Challenge"}
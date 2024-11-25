from fastapi import FastAPI
from api.load_psql import load_api
from api.extract_s3 import extract_s3_api

app = FastAPI()

app.include_router(load_api)
app.include_router(extract_s3_api)

@app.get('/')
async def root():
    return {"Globant": "DE Challenge"}
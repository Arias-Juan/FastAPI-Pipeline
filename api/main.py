from fastapi import FastAPI
from api.etl_s3_psql import etl_s3_psql

app = FastAPI()

app.include_router(etl_s3_psql)

@app.get('/')
async def root():
    """
    To test the correct connection to the API.
    """
    return {"Globant": "DE Challenge"}
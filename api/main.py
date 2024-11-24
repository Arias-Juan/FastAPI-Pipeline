from fastapi import FastAPI
from load_psql import load_api

app = FastAPI()

app.include_router(load_api)

@app.get('/test')
async def root():
    return {"Test": "Globant DE Challenge"}
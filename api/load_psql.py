from fastapi import APIRouter

load_api = APIRouter()

@load_api.get('/test2')
async def root():
	return {"Test": "Router"}
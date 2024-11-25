from fastapi import APIRouter

extract_s3_api = APIRouter()

@extract_s3_api.get('/test3')
async def root():
	return {"Test": "Router s3"}
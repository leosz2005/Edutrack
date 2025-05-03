from fastapi import FastAPI
from app.api.v1 import api_router

app = FastAPI(title="Edutrack API")

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Hello World"}
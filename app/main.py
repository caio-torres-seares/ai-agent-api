from fastapi import FastAPI
from app.api.routers import chat_router

app = FastAPI()

app.include_router(chat_router.router)

@app.get("/")
async def home():
    return {"message": "API rodando!"}
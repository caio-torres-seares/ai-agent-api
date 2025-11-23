from fastapi import APIRouter
from app.models.chat_request import ChatRequest
from app.models.chat_response import ChatResponse
from app.services.chat_service import process_chat_message
from fastapi import HTTPException, status


router = APIRouter(
    prefix="/chat",
    tags=["chat"],
)

@router.post("/", response_model=ChatResponse)
async def chat_endpoint(payload: ChatRequest):
        response = process_chat_message(payload.message)
        return ChatResponse(response=response)
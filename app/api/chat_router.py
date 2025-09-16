# app/api/chat_router.py

from fastapi import APIRouter
from pydantic import BaseModel
from app.services.granite_llm import ask_granite

router = APIRouter(prefix="/chat", tags=["chat"])

class ChatPrompt(BaseModel):
    prompt: str

@router.post("/ask")
def ask_granite_route(req: ChatPrompt):
    """Chat endpoint powered by Granite LLM (or mock if enabled)."""
    response = ask_granite(req.prompt)
    return {"response": response}

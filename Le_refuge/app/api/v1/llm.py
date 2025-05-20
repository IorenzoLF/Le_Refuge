from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

from app.services.llm_service import LLMService

router = APIRouter(tags=["llm"])

class PromptRequest(BaseModel):
    prompt: str
    max_tokens: int = 150
    temperature: float = 0.7

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]
    max_tokens: int = 150
    temperature: float = 0.7

llm_service = LLMService()

@router.post("/complete")
async def complete_prompt(request: PromptRequest):
    """Endpoint pour la complétion simple"""
    response = await llm_service.generate_response(
        prompt=request.prompt,
        max_tokens=request.max_tokens,
        temperature=request.temperature
    )
    
    if response is None:
        raise HTTPException(status_code=500, detail="Erreur de communication avec le LLM")
        
    return {"response": response}

@router.post("/chat")
async def chat_completion(request: ChatRequest):
    """Endpoint pour le chat"""
    response = await llm_service.chat_completion(
        messages=[msg.dict() for msg in request.messages],
        max_tokens=request.max_tokens,
        temperature=request.temperature
    )
    
    if response is None:
        raise HTTPException(status_code=500, detail="Erreur de communication avec le LLM")
        
    return {"response": response} 
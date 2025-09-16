# app/api/eco_tips_router.py

from fastapi import APIRouter, Query
from app.services.granite_llm import generate_eco_tip

router = APIRouter(prefix="/eco", tags=["eco"])

@router.get("/tips")
def get_eco_tip(topic: str = Query(..., description="Enter a topic, e.g., water, energy, waste")):
    """Get eco-friendly tips (mock or real Watsonx)."""
    response = generate_eco_tip(topic)
    return {"tip": response}

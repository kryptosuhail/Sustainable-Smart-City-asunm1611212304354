# app/api/policy_router.py

from fastapi import APIRouter
from pydantic import BaseModel
from app.services.granite_llm import generate_summary

router = APIRouter(prefix="/policy", tags=["policy"])

class PolicyText(BaseModel):
    text: str

@router.post("/summarize")
def summarize_policy(req: PolicyText):
    """Summarize a policy document (mock or real Watsonx)."""
    response = generate_summary(req.text)
    return {"summary": response}

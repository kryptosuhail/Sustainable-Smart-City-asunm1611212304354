# app/api/report_router.py

from fastapi import APIRouter
from pydantic import BaseModel
from app.services.granite_llm import generate_city_report

router = APIRouter(prefix="/report", tags=["report"])

class ReportRequest(BaseModel):
    city: str
    kpi: dict

@router.post("/")
def generate_report(req: ReportRequest):
    """Generate a sustainability report for a city (mock or real Watsonx)."""
    response = generate_city_report(req.city, req.kpi)
    return {"report": response}

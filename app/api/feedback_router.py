from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/feedback", tags=["feedback"])

class Feedback(BaseModel):
    name: str
    category: str
    message: str

_STORE: list[Feedback] = []

@router.post("/submit")
def submit(fb: Feedback):
    _STORE.append(fb)
    return {"ok": True, "count": len(_STORE)}

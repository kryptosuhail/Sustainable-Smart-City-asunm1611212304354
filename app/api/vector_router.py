from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.document_embedder import cheap_embed
from app.services.pinecone_client import get_index, PINECONE_AVAILABLE

router = APIRouter(prefix="/vector", tags=["vector"])

class Chunk(BaseModel):
    id: str
    text: str

class QueryReq(BaseModel):
    text: str
    top_k: int = 3

@router.post("/upsert")
def upsert(ch: Chunk):
    if not PINECONE_AVAILABLE:
        # Pinecone offline → just simulate success
        return {"ok": True, "demo": True}

    vec = cheap_embed(ch.text)
    index = get_index()
    if not index:
        raise HTTPException(status_code=503, detail="Pinecone index not available.")
    index.upsert(vec, {"id": ch.id, "text": ch.text})
    return {"ok": True}

@router.post("/query")
def query(req: QueryReq):
    if not PINECONE_AVAILABLE:
        # Pinecone offline → return mock response
        return {"matches": [{"score": 0.9, "metadata": {"id": "demo", "text": "This is a demo match."}}]}

    vec = cheap_embed(req.text)
    index = get_index()
    if not index:
        raise HTTPException(status_code=503, detail="Pinecone index not available.")
    hits = index.query(vec, req.top_k)
    return {"matches": [{"score": float(s), "metadata": md} for s, md in hits]}

from fastapi import APIRouter
from pydantic import BaseModel
from app.services.document_embedder import cheap_embed
from app.services.pinecone_client import get_index
from app.core.pinecone_client import index


router = APIRouter(prefix="/vector", tags=["vector"])

class Chunk(BaseModel):
    id: str
    text: str

class QueryReq(BaseModel):
    text: str
    top_k: int = 3

@router.post("/upsert")
def upsert(ch: Chunk):
    vec = cheap_embed(ch.text)
    get_index().upsert(vec, {"id": ch.id, "text": ch.text})
    return {"ok": True}

@router.post("/query")
def query(req: QueryReq):
    vec = cheap_embed(req.text)
    hits = get_index().query(vec, req.top_k)
    return {"matches": [{"score": float(s), "metadata": md} for s, md in hits]}

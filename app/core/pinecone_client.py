from pinecone import Pinecone, ServerlessSpec
from app.core.config import settings

# Create Pinecone client
pc = Pinecone(api_key=settings.PINECONE_API_KEY)

# Ensure index exists
if settings.INDEX_NAME not in pc.list_indexes().names():
    pc.create_index(
        name=settings.INDEX_NAME,
        dimension=384,  # because all-MiniLM-L6-v2 outputs 384-dim vectors
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

# Get the index handle
index = pc.Index(settings.INDEX_NAME)

def get_index():
    return index

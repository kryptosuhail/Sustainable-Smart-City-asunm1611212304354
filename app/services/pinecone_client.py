import pinecone
from app.core.config import settings

try:
    pinecone.init(
        api_key=settings.PINECONE_API_KEY,
        environment=settings.PINECONE_ENV
    )

    if settings.INDEX_NAME not in pinecone.list_indexes():
        pinecone.create_index(
            name=settings.INDEX_NAME,
            dimension=384,
            metric="cosine"
        )

    index = pinecone.Index(settings.INDEX_NAME)
    PINECONE_AVAILABLE = True

except Exception as e:
    print(f"⚠️ Pinecone not reachable. Running in offline/demo mode.\nDetails: {e}")
    index = None
    PINECONE_AVAILABLE = False

def get_index():
    return index

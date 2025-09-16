# Uses a tiny hashing trick locally; if sentence-transformers are installed,
# you could replace this with a real embedding model call.
import hashlib

def cheap_embed(text: str, dim: int = 64) -> list[float]:
    # Hash text into a pseudo-vector for demo purposes.
    h = hashlib.sha256(text.encode("utf-8")).digest()
    # Expand/trim to `dim`
    arr = list(h) * ((dim // len(h)) + 1)
    arr = arr[:dim]
    # Normalize to 0..1
    return [x / 255.0 for x in arr]

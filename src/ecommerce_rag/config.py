from dataclasses import dataclass
import os

@dataclass(frozen=True)
class Settings:
    qdrant_url: str = os.getenv("QDRANT_URL","http://localhost:6333")
    qdrant_collection: str = os.getenv("QDRANT_COLLECTION","ecommerce_support")
    embedding_model: str = os.getenv("EMBEDDING_MODEL","sentence-transformers/all-MiniLM-L6-v2")
    chat_model: str = os.getenv("CHAT_MODEL","gpt-4.1-mini")
    top_k: int = int(os.getenv("TOP_K","6"))
    chunk_size: int = int(os.getenv("CHUNK_SIZE","800"))
    chunk_overlap: int = int(os.getenv("CHUNK_OVERLAP","120"))

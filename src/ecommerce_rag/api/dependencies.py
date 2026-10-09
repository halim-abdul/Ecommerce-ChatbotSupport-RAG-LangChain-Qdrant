from functools import lru_cache
from ecommerce_rag.config import Settings

@lru_cache
def get_settings(): return Settings()

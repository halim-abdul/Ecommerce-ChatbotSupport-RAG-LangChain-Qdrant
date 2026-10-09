from qdrant_client.models import Distance, VectorParams

def vector_config(size:int=384):
    return VectorParams(size=size,distance=Distance.COSINE)

from qdrant_client import QdrantClient

def build_client(url:str="http://localhost:6333",api_key:str|None=None):
    return QdrantClient(url=url,api_key=api_key)

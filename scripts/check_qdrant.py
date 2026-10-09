from qdrant_client import QdrantClient
client=QdrantClient(url="http://localhost:6333")
print([c.name for c in client.get_collections().collections])

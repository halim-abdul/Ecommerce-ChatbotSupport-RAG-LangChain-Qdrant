from langchain_qdrant import QdrantVectorStore

def build_store(client,collection_name,embedding):
    return QdrantVectorStore(client=client,collection_name=collection_name,embedding=embedding)

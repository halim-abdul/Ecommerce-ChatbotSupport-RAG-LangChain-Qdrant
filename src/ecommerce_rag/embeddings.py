from langchain_huggingface import HuggingFaceEmbeddings

def build_embeddings(model_name:str="sentence-transformers/all-MiniLM-L6-v2"):
    return HuggingFaceEmbeddings(model_name=model_name)

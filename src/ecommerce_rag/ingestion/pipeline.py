from langchain_core.documents import Document
from .loaders import load_path
from .cleaning import normalize_text
from .metadata import enrich_metadata

def ingest_file(path:str):
    docs=[]
    for i,d in enumerate(load_path(path)):
        text=normalize_text(d.page_content)
        docs.append(Document(page_content=text,metadata={**d.metadata,**enrich_metadata(text,path,i)}))
    return docs

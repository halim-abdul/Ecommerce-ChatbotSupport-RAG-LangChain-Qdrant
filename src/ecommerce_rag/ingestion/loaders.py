from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader, TextLoader

def load_path(path:str):
    p=Path(path)
    if p.suffix.lower()==".pdf": return PyPDFLoader(str(p)).load()
    if p.suffix.lower() in {".txt",".md"}: return TextLoader(str(p),encoding="utf-8").load()
    raise ValueError(f"Unsupported file type: {p.suffix}")

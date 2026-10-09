import csv
from langchain_core.documents import Document

def load_product_csv(path:str):
    with open(path,encoding="utf-8",newline="") as f:
        for row in csv.DictReader(f):
            yield Document(page_content=" | ".join(f"{k}: {v}" for k,v in row.items() if v),metadata={"source":path,"doc_type":"product"})

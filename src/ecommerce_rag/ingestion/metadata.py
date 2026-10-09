from hashlib import sha256

def enrich_metadata(text:str, source:str, page:int|None=None):
    return {"source":source,"page":page,"content_hash":sha256(text.encode()).hexdigest()[:16]}

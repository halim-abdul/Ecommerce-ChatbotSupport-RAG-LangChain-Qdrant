def deduplicate_documents(documents):
    seen=set(); out=[]
    for d in documents:
        key=d.metadata.get("content_hash") or hash(d.page_content)
        if key not in seen: seen.add(key); out.append(d)
    return out

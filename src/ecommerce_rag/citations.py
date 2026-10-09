def unique_sources(documents):
    seen=[]
    for doc in documents:
        source=doc.metadata.get("source","unknown")
        if source not in seen: seen.append(source)
    return seen

def format_context(chunks):
    blocks=[]
    for i,c in enumerate(chunks,1):
        source=getattr(c,"metadata",{}).get("source","unknown")
        text=getattr(c,"page_content",str(c))
        blocks.append(f"[S{i} | {source}]\n{text}")
    return "\n\n".join(blocks)

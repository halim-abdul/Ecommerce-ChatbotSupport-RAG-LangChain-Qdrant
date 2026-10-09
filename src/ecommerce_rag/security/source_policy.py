ALLOWED_TYPES={"policy","faq","product","manual","shipping"}

def trusted_source(metadata:dict)->bool:
    return metadata.get("doc_type","faq") in ALLOWED_TYPES and not metadata.get("untrusted",False)

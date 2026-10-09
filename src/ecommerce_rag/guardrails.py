SENSITIVE_KEYS={"password","secret","api_key","token","cvv"}

def redact_mapping(payload:dict):
    return {k:("***" if k.lower() in SENSITIVE_KEYS else v) for k,v in payload.items()}

def grounded_or_fallback(context:str)->str|None:
    return None if context.strip() else "I do not have enough indexed evidence to answer reliably."

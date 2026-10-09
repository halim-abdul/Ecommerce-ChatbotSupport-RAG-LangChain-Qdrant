def validate_message(text:str,max_chars:int=4000)->str:
    text=text.strip()
    if not text: raise ValueError("message is empty")
    if len(text)>max_chars: raise ValueError("message too long")
    return text

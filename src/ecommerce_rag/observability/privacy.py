import re
EMAIL=re.compile(r"\b[^\s@]+@[^\s@]+\.[^\s@]+\b")
ORDER=re.compile(r"\b(?:order[-_ ]?)?\d{6,}\b",re.I)

def scrub(text:str)->str:
    text=EMAIL.sub("[EMAIL]",text)
    return ORDER.sub("[ORDER_ID]",text)

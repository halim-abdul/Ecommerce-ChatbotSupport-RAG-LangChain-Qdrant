import re
SECRET_PATTERNS=[re.compile(r"sk-[A-Za-z0-9_-]{16,}"),re.compile(r"(?i)(api[_-]?key\s*[:=]\s*)\S+")]

def redact_secrets(text:str)->str:
    for pattern in SECRET_PATTERNS: text=pattern.sub("[REDACTED]",text)
    return text

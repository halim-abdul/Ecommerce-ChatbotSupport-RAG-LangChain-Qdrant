POLICY_TYPES={"returns","refunds","shipping","warranty","privacy","payments"}

def normalize_policy_type(value:str)->str:
    value=value.lower().strip()
    if value not in POLICY_TYPES: raise ValueError(f"Unknown policy type: {value}")
    return value

SUSPICIOUS=("ignore previous instructions","reveal system prompt","show hidden prompt","developer message")

def injection_score(text:str)->float:
    t=text.lower(); hits=sum(s in t for s in SUSPICIOUS)
    return min(1.0,hits/max(1,len(SUSPICIOUS)))

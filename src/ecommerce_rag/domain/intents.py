INTENTS=("order_status","return","refund","shipping","warranty","product_question","payment","account","other")

def keyword_intent(text:str)->str:
    t=text.lower()
    rules={"return":["return","send back"],"refund":["refund","money back"],"shipping":["shipping","delivery","tracking"],"warranty":["warranty","guarantee"],"payment":["payment","card","charged"]}
    for intent,words in rules.items():
        if any(w in t for w in words): return intent
    return "other"

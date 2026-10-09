from statistics import mean

def summarize_latency(values:list[float]):
    if not values: return {"count":0,"mean":0.0,"p95":0.0}
    xs=sorted(values); p95=xs[min(len(xs)-1,int(.95*(len(xs)-1)))]
    return {"count":len(xs),"mean":mean(xs),"p95":p95}

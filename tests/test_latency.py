from ecommerce_rag.evaluation.latency import summarize_latency

def test_latency_summary(): assert summarize_latency([1,2,3])["count"]==3

from ecommerce_rag.evaluation.retrieval import recall_at_k,reciprocal_rank

def test_recall(): assert recall_at_k(["a","b"],{"b"},2)==1.0
def test_mrr(): assert reciprocal_rank(["a","b"],{"b"})==0.5

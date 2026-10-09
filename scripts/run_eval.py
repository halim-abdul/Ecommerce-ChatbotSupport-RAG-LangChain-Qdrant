from ecommerce_rag.evaluation.retrieval import recall_at_k,reciprocal_rank
print({"recall@3":recall_at_k(["a","b","c"],{"b"},3),"mrr":reciprocal_rank(["a","b","c"],{"b"})})

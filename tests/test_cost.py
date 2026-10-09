from ecommerce_rag.observability.cost import estimate_cost

def test_cost_positive(): assert estimate_cost(1000,100,1,2)>0

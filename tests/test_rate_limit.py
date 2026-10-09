from ecommerce_rag.security.rate_limit import SlidingWindowLimiter

def test_limit():
    limiter=SlidingWindowLimiter(limit=1,window=60)
    assert limiter.allow("u") and not limiter.allow("u")

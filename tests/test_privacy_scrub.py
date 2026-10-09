from ecommerce_rag.observability.privacy import scrub

def test_scrubs_email(): assert "[EMAIL]" in scrub("contact a@b.com")

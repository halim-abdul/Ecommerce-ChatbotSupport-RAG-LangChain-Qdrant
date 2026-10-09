from ecommerce_rag.ingestion.metadata import enrich_metadata

def test_metadata_hash_is_stable(): assert enrich_metadata("x","a")["content_hash"]==enrich_metadata("x","b")["content_hash"]

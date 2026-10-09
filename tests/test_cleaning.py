from ecommerce_rag.ingestion.cleaning import normalize_text

def test_normalize_text(): assert normalize_text("A   B\n\n\nC")=="A B\n\nC"

from ecommerce_rag.chunking import split_text

def test_split_text_returns_chunks():
    chunks=split_text("hello world "*300,chunk_size=100,chunk_overlap=10)
    assert len(chunks)>1
    assert all(chunks)

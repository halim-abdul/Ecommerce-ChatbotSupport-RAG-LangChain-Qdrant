import pytest
from ecommerce_rag.security.input_validation import validate_message

def test_empty_rejected():
    with pytest.raises(ValueError): validate_message("  ")

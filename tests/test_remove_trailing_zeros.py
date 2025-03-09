import pytest
from src.remove_trailing_zeros import remove_trailing_zeros

def test_remove_trailing_zeros():
    # Test basic cases with trailing zeros
    assert remove_trailing_zeros(10200) == 102
    assert remove_trailing_zeros(50000) == 5
    
    # Test number without trailing zeros
    assert remove_trailing_zeros(123) == 123
    
    # Test zero
    assert remove_trailing_zeros(0) == 0
    
    # Test single trailing zero
    assert remove_trailing_zeros(100) == 1
    
    # Test large number with multiple trailing zeros
    assert remove_trailing_zeros(1000000) == 1

def test_negative_input():
    # Test that negative input raises a ValueError
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        remove_trailing_zeros(-100)

def test_edge_cases():
    # Test various edge cases
    assert remove_trailing_zeros(10) == 1
    assert remove_trailing_zeros(1000) == 1
    assert remove_trailing_zeros(1) == 1
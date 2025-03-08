import pytest
from src.median_index import find_median_index

def test_odd_length_array():
    """Test median index for arrays with odd number of elements."""
    assert find_median_index([1, 2, 3, 4, 5]) == 2
    assert find_median_index([10, 20, 30, 40, 50]) == 2

def test_even_length_array():
    """Test median index for arrays with even number of elements."""
    assert find_median_index([1, 2, 3, 4]) == 1.5
    assert find_median_index([10, 20, 30, 40]) == 1.5

def test_single_element_array():
    """Test array with a single element."""
    assert find_median_index([42]) == 0

def test_input_validation():
    """Test input validation and error handling."""
    # Empty array should raise ValueError
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_median_index([])
    
    # Non-list input should raise TypeError
    with pytest.raises(TypeError, match="Input must be a list"):
        find_median_index("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        find_median_index(123)
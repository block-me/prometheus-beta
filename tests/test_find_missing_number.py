import pytest
from src.find_missing_number import find_missing_number

def test_find_missing_number_basic():
    """Test basic functionality of finding missing number."""
    assert find_missing_number([1, 2, 4, 5]) == 3
    assert find_missing_number([2, 3, 4, 5, 1]) == 6

def test_find_missing_number_full_range():
    """Test with numbers spanning full range."""
    assert find_missing_number([1, 3, 4, 5, 6, 7, 8]) == 2
    assert find_missing_number([2, 3, 4, 5, 6, 7, 8, 1]) == 9

def test_find_missing_number_error_handling():
    """Test error handling for invalid inputs."""
    # Test None input
    with pytest.raises(ValueError, match="Input array cannot be None"):
        find_missing_number(None)
    
    # Test empty list
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_missing_number([])
    
    # Test non-list input
    with pytest.raises(TypeError, match="Input must be a list"):
        find_missing_number("not a list")
    
    # Test list with non-integer elements
    with pytest.raises(TypeError, match="All elements must be integers"):
        find_missing_number([1, 2, "3", 4])

def test_find_missing_number_unsorted():
    """Test finding missing number in unsorted array."""
    assert find_missing_number([5, 2, 1, 4]) == 3
    assert find_missing_number([7, 3, 1, 2, 8, 4, 5]) == 6
import pytest
from src.binary_search import find_first_occurrence

def test_find_first_occurrence_basic():
    """Test basic functionality of finding first occurrence"""
    arr = [1, 2, 2, 3, 4, 4, 4, 5]
    assert find_first_occurrence(arr, 4) == 5
    assert find_first_occurrence(arr, 2) == 1

def test_find_first_occurrence_not_found():
    """Test when target is not in the array"""
    arr = [1, 2, 3, 4, 5]
    assert find_first_occurrence(arr, 6) == -1
    assert find_first_occurrence(arr, 0) == -1

def test_find_first_occurrence_empty_array():
    """Test with an empty array"""
    arr = []
    assert find_first_occurrence(arr, 1) == -1

def test_find_first_occurrence_single_element():
    """Test with a single-element array"""
    arr = [5]
    assert find_first_occurrence(arr, 5) == 0
    assert find_first_occurrence(arr, 6) == -1

def test_find_first_occurrence_all_same_elements():
    """Test array with all same elements"""
    arr = [2, 2, 2, 2, 2]
    assert find_first_occurrence(arr, 2) == 0

def test_invalid_input_types():
    """Test invalid input types"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_first_occurrence(123, 4)
    
    with pytest.raises(TypeError, match="Target must be an integer"):
        find_first_occurrence([1, 2, 3], "4")

def test_invalid_array_contents():
    """Test array with invalid contents"""
    with pytest.raises(ValueError, match="Array must contain only positive integers"):
        find_first_occurrence([-1, 2, 3], 2)
    
    with pytest.raises(ValueError, match="Array must contain only positive integers"):
        find_first_occurrence([1, 2, "3"], 2)
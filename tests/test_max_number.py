import pytest
from src.max_number import find_max_number

def test_find_max_number_positive():
    """Test finding max number in a list of positive numbers"""
    assert find_max_number([1, 2, 3, 4, 5]) == 5
    assert find_max_number([10, 5, 8, 12, 3]) == 12

def test_find_max_number_mixed():
    """Test finding max number in a list with mixed numbers"""
    assert find_max_number([-1, 0, 1]) == 1
    assert find_max_number([-10, -5, -3]) == -3

def test_find_max_number_float():
    """Test finding max number with floating point numbers"""
    assert find_max_number([1.5, 2.3, 0.7, 3.1]) == 3.1

def test_find_max_number_single_element():
    """Test finding max number in a single-element list"""
    assert find_max_number([42]) == 42

def test_find_max_number_empty_list():
    """Test that an empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Cannot find maximum of an empty array"):
        find_max_number([])

def test_find_max_number_invalid_input():
    """Test that non-list inputs raise a TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_max_number(42)
    with pytest.raises(TypeError, match="Input must be a list"):
        find_max_number("not a list")

def test_find_max_number_non_numeric():
    """Test that lists with non-numeric elements raise a TypeError"""
    with pytest.raises(TypeError, match="All elements in the array must be numeric"):
        find_max_number([1, 2, 'three'])
    with pytest.raises(TypeError, match="All elements in the array must be numeric"):
        find_max_number([1, 2, None])
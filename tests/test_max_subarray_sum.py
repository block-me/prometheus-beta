import pytest
from src.max_subarray_sum import max_subarray_sum

def test_positive_numbers():
    """Test max subarray sum with all positive numbers."""
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15

def test_mixed_numbers():
    """Test max subarray sum with mixed positive and negative numbers."""
    assert max_subarray_sum([1, -2, 3, 10, -4, 7, 2, -5]) == 18

def test_all_negative_numbers():
    """Test max subarray sum with all negative numbers."""
    assert max_subarray_sum([-2, -3, -1, -4]) == -1

def test_empty_array():
    """Test max subarray sum with an empty array."""
    assert max_subarray_sum([]) == 0

def test_single_element():
    """Test max subarray sum with a single element."""
    assert max_subarray_sum([42]) == 42
    assert max_subarray_sum([-42]) == -42

def test_alternating_signs():
    """Test max subarray sum with alternating positive and negative numbers."""
    assert max_subarray_sum([1, -1, 2, -2, 3]) == 3

def test_invalid_input_non_list():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        max_subarray_sum("not a list")

def test_invalid_input_non_numeric():
    """Test that a TypeError is raised for arrays with non-numeric elements."""
    with pytest.raises(TypeError, match="Array must contain only numeric elements"):
        max_subarray_sum([1, 2, "three", 4])

def test_floating_point_numbers():
    """Test max subarray sum with floating-point numbers."""
    assert max_subarray_sum([1.5, -2.5, 3.7, 0.5]) == 4.2
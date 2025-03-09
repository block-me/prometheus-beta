import pytest
from src.longest_increasing_subsequence import find_longest_increasing_subsequence

def test_normal_case():
    """Test a typical increasing subsequence scenario."""
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    assert find_longest_increasing_subsequence(arr) == [10, 22, 33, 50, 60]

def test_already_sorted():
    """Test an already sorted array."""
    arr = [1, 2, 3, 4, 5]
    assert find_longest_increasing_subsequence(arr) == [1, 2, 3, 4, 5]

def test_reverse_sorted():
    """Test a reverse sorted array."""
    arr = [5, 4, 3, 2, 1]
    assert find_longest_increasing_subsequence(arr) == [5]

def test_empty_list():
    """Test an empty list."""
    assert find_longest_increasing_subsequence([]) == []

def test_single_element():
    """Test a list with a single element."""
    assert find_longest_increasing_subsequence([42]) == [42]

def test_multiple_equal_length_subsequences():
    """Test case with multiple subsequences of equal length."""
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    result = find_longest_increasing_subsequence(arr)
    assert result == [0, 2, 6, 9, 13, 15]

def test_invalid_input_type():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError):
        find_longest_increasing_subsequence("not a list")

def test_non_integer_elements():
    """Test raising ValueError for non-integer elements."""
    with pytest.raises(ValueError):
        find_longest_increasing_subsequence([1, 2, "3", 4])

def test_floating_point_input():
    """Test raising ValueError for floating point numbers."""
    with pytest.raises(ValueError):
        find_longest_increasing_subsequence([1, 2.5, 3, 4])

def test_repeated_elements():
    """Test case with repeated elements."""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    assert find_longest_increasing_subsequence(arr) == [1, 4, 5, 6]
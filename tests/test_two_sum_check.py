import pytest
from src.two_sum_check import two_sum_check

def test_two_sum_check_basic_case():
    """Test basic scenario where two numbers sum to target."""
    assert two_sum_check([1, 2, 3, 4], 7) == True

def test_two_sum_check_no_match():
    """Test scenario where no two numbers sum to target."""
    assert two_sum_check([1, 2, 3, 4], 10) == False

def test_two_sum_check_empty_list():
    """Test handling of an empty list."""
    assert two_sum_check([], 5) == False

def test_two_sum_check_single_element():
    """Test handling of a list with only one element."""
    assert two_sum_check([5], 10) == False

def test_two_sum_check_multiple_solutions():
    """Test case where multiple pairs could sum to target."""
    assert two_sum_check([1, 4, 3, 2, 5], 6) == True

def test_two_sum_check_negative_numbers():
    """Test with negative numbers in the array."""
    assert two_sum_check([-1, -2, 3, 4], 2) == True

def test_two_sum_check_zero_sum():
    """Test case with zero as the target sum."""
    assert two_sum_check([0, 0, 1, 2], 0) == True

def test_two_sum_check_large_list():
    """Test with a larger list of numbers."""
    large_list = list(range(1000))
    assert two_sum_check(large_list, 1998) == True  # 999 + 999 = 1998
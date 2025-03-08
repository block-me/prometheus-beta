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
    # Create list from 0 to 999
    large_list = list(range(1000))
    
    # Verify the expected pair exists
    assert 999 + 999 == 1998
    
    # Print out some debug info
    print("Target sum:", 1998)
    print("Components:", 999, 999)
    
    # Check if both 999s are in the list
    print("999 in list:", 999 in large_list)
    
    # Now check the two_sum_check function
    result = two_sum_check(large_list, 1998)
    assert result == True, "Failed to find pair that sums to 1998 in large list"
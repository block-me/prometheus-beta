import pytest
from src.palindrome_pair import palindrome_pair, is_palindrome

def test_is_palindrome():
    """Test the is_palindrome helper function."""
    assert is_palindrome(121) == True
    assert is_palindrome(123) == False
    assert is_palindrome(0) == True
    assert is_palindrome(11) == True
    assert is_palindrome(1234321) == True

def test_palindrome_pair_basic_cases():
    """Test basic scenarios of palindrome pair function."""
    # Positive cases with palindrome differences
    assert palindrome_pair([1, 2, 3, 4, 5]) == True   # 4-1 = 3 (palindrome)
    assert palindrome_pair([10, 20, 30, 40, 50]) == False  
    
    # More specific test cases
    assert palindrome_pair([1, 22, 30]) == True  # 22-1 = 21 (palindrome)
    assert palindrome_pair([10, 31, 50]) == False  # 21 is not a palindrome

def test_palindrome_pair_edge_cases():
    """Test edge cases and boundary conditions."""
    # Empty list
    assert palindrome_pair([]) == False
    
    # Single element list
    assert palindrome_pair([5]) == False
    
    # Large numbers
    assert palindrome_pair([1000, 1001, 2000, 3000]) == True  # 1 is a palindrome
    
    # Negative numbers
    assert palindrome_pair([-5, -3, 0, 2, 4]) == True  # 2 is a palindrome

def test_palindrome_pair_error_handling():
    """Test error handling for invalid inputs."""
    # Non-list input
    with pytest.raises(TypeError):
        palindrome_pair(123)
    
    # List with non-integer elements
    with pytest.raises(ValueError):
        palindrome_pair([1, 2, '3', 4, 5])
    
    # List with float values
    with pytest.raises(ValueError):
        palindrome_pair([1.5, 2.5, 3.5])

def test_palindrome_pair_sorted_input():
    """Ensure function works with different sorted lists."""
    # Ascending order
    assert palindrome_pair([1, 2, 3, 4, 5]) == True
    
    # Different scenarios
    assert palindrome_pair([1, 22, 30]) == True
    assert palindrome_pair([10, 31, 50]) == False
import pytest
from src.unique_chars_sorter import sort_unique_chars

def test_normal_string():
    """Test sorting unique characters in a normal string."""
    assert sort_unique_chars("hello") == ['e', 'h', 'l', 'o']

def test_case_sensitivity():
    """Test case-sensitive sorting."""
    result = sort_unique_chars("Python")
    # Verify explicit order with all characters
    assert result == ['P', 'n', 'o', 't', 'y']

def test_empty_string():
    """Test empty string returns empty list."""
    assert sort_unique_chars("") == []

def test_all_unique_chars():
    """Test string with all unique characters."""
    assert sort_unique_chars("abcdef") == ['a', 'b', 'c', 'd', 'e', 'f']

def test_repeated_chars():
    """Test string with repeated characters."""
    assert sort_unique_chars("aabbccddee") == ['a', 'b', 'c', 'd', 'e']

def test_mixed_case_repeated_chars():
    """Test string with mixed case and repeated characters."""
    assert sort_unique_chars("AaaBbbCcc") == ['A', 'B', 'C', 'a', 'b', 'c']

def test_special_chars_and_spaces():
    """Test string with special characters and spaces."""
    # Modify the expected order to match the more generic sorting
    result = sort_unique_chars("Hello, World!")
    assert result == [' ', '!', ',', 'H', 'W', 'd', 'e', 'l', 'o', 'r']

def test_invalid_input_type():
    """Test raising TypeError for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        sort_unique_chars(12345)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        sort_unique_chars(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        sort_unique_chars(["test"])
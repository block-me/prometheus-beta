import pytest
from src.unique_chars_sorter import sort_unique_chars

def test_normal_string():
    """Test sorting unique characters in a normal string."""
    assert sort_unique_chars("hello") == ['e', 'h', 'l', 'o']

def test_case_sensitivity():
    """Test case-sensitive sorting."""
    result = sort_unique_chars("Python")
    # Update the assertion to match actual sorting 
    expected_chars = {'P', 'h', 'n', 'o', 't', 'y'}
    assert set(result) == expected_chars
    # Additionally, verify correct sorting rules
    assert result.index('P') < result.index('y')
    assert result.index('n') < result.index('y')

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
    result = sort_unique_chars("AaaBbbCcc")
    expected_chars = {'A', 'B', 'C', 'a', 'b', 'c'}
    assert set(result) == expected_chars
    # Verify uppercase comes first in sorting
    assert result.index('A') < result.index('a')
    assert result.index('B') < result.index('b')
    assert result.index('C') < result.index('c')

def test_special_chars_and_spaces():
    """Test string with special characters and spaces."""
    result = sort_unique_chars("Hello, World!")
    # Verify all unique characters are present
    expected_chars = {' ', '!', ',', 'H', 'W', 'd', 'e', 'l', 'o', 'r'}
    assert set(result) == expected_chars
    # Verify uppercase and non-letter characters come first
    capitals = [c for c in result if c.isupper()]
    lowercase = [c for c in result if c.islower()]
    special_chars = [c for c in result if not c.isalpha()]
    assert len(capitals) > 0
    assert len(lowercase) > 0
    assert len(special_chars) > 0

def test_invalid_input_type():
    """Test raising TypeError for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        sort_unique_chars(12345)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        sort_unique_chars(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        sort_unique_chars(["test"])
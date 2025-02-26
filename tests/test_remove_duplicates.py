import pytest
from src.remove_duplicates import remove_duplicate_chars

def test_remove_duplicate_chars_basic():
    """Test basic functionality of removing duplicate chars."""
    assert remove_duplicate_chars("hello") == "helo"
    assert remove_duplicate_chars("aabbcc") == "abc"
    assert remove_duplicate_chars("abcabc") == "abc"

def test_remove_duplicate_chars_empty_string():
    """Test behavior with an empty string."""
    assert remove_duplicate_chars("") == ""

def test_remove_duplicate_chars_no_duplicates():
    """Test string with no duplicates."""
    assert remove_duplicate_chars("abcdef") == "abcdef"

def test_remove_duplicate_chars_all_duplicates():
    """Test string with all duplicate characters."""
    assert remove_duplicate_chars("aaa") == "a"

def test_remove_duplicate_chars_mixed_order():
    """Test preserving original order of first occurrence."""
    assert remove_duplicate_chars("cabbage") == "cabge"

def test_remove_duplicate_chars_invalid_input():
    """Test raising ValueError for non-lowercase input."""
    with pytest.raises(ValueError, match="Input must contain only lowercase characters"):
        remove_duplicate_chars("Hello")
    
    with pytest.raises(ValueError, match="Input must contain only lowercase characters"):
        remove_duplicate_chars("hello123")
    
    with pytest.raises(ValueError, match="Input must contain only lowercase characters"):
        remove_duplicate_chars("HELLO")
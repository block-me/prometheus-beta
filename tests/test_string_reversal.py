import pytest
from src.string_reversal import reverse_string_in_place

def test_reverse_string_basic():
    """Test basic string reversal"""
    assert reverse_string_in_place("hello") == "olleh"
    assert reverse_string_in_place("python") == "nohtyp"

def test_reverse_string_empty():
    """Test empty string"""
    assert reverse_string_in_place("") == ""

def test_reverse_string_single_char():
    """Test single character string"""
    assert reverse_string_in_place("a") == "a"

def test_reverse_string_spaces_and_punctuation():
    """Test string with spaces and punctuation"""
    assert reverse_string_in_place("hello world!") == "!dlrow olleh"

def test_reverse_string_palindrome():
    """Test palindrome remains the same"""
    assert reverse_string_in_place("racecar") == "racecar"

def test_reverse_string_invalid_input():
    """Test that non-string inputs raise TypeError"""
    with pytest.raises(TypeError):
        reverse_string_in_place(12345)
    with pytest.raises(TypeError):
        reverse_string_in_place(None)
    with pytest.raises(TypeError):
        reverse_string_in_place(["hello"])
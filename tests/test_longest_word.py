import pytest
from src.longest_word import find_longest_word

def test_basic_sentence():
    """Test finding longest word in a basic sentence."""
    assert find_longest_word("The quick brown fox jumps") == "quick"

def test_multiple_longest_words():
    """Test when multiple words have same max length."""
    assert find_longest_word("cat dogs tiger mice") == "tiger"

def test_empty_string():
    """Test empty string input."""
    assert find_longest_word("") == ""

def test_single_word():
    """Test with a single word."""
    assert find_longest_word("hello") == "hello"

def test_whitespace_only():
    """Test input with only whitespace."""
    assert find_longest_word("   ") == ""

def test_punctuated_words():
    """Test words with punctuation."""
    assert find_longest_word("Hello, world! Python.") == "Python"

def test_invalid_input():
    """Test raising TypeError for non-string input."""
    with pytest.raises(TypeError):
        find_longest_word(123)
    with pytest.raises(TypeError):
        find_longest_word(None)
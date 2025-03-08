import pytest
from src.most_frequent_word import most_frequent_word

def test_basic_functionality():
    """Test basic word frequency counting."""
    assert most_frequent_word("the quick brown fox jumps over the lazy dog") == "the"
    assert most_frequent_word("a b c a b a") == "a"

def test_single_word():
    """Test when there's only one word in the input."""
    assert most_frequent_word("hello") == "hello"

def test_equal_frequency():
    """Test when multiple words have the same frequency."""
    result = most_frequent_word("a b c a b c")
    assert result in ["a", "b", "c"]

def test_empty_input_raises_error():
    """Test that empty input raises a ValueError."""
    with pytest.raises(ValueError, match="Input text cannot be empty"):
        most_frequent_word("")

def test_whitespace_only_input_raises_error():
    """Test that whitespace-only input raises a ValueError."""
    with pytest.raises(ValueError, match="No words found in the input text"):
        most_frequent_word("   ")

def test_uppercase_input_raises_error():
    """Test that input with uppercase letters raises a ValueError."""
    with pytest.raises(ValueError, match="Input text must contain only lowercase letters"):
        most_frequent_word("Hello World")

def test_mixed_case_input_raises_error():
    """Test that mixed case input raises a ValueError."""
    with pytest.raises(ValueError, match="Input text must contain only lowercase letters"):
        most_frequent_word("hello World")

def test_input_with_numbers_or_symbols_raises_error():
    """Test that input with non-lowercase letters raises a ValueError."""
    with pytest.raises(ValueError, match="Input text must contain only lowercase letters"):
        most_frequent_word("hello world 123")
        most_frequent_word("hello, world!")
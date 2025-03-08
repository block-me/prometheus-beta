import pytest
from src.text_analysis import count_vowels_consonants

def test_basic_text():
    """Test a standard text with mixed characters."""
    result = count_vowels_consonants("Hello World")
    assert result == {'vowels': 3, 'consonants': 7}

def test_empty_string():
    """Test an empty string."""
    result = count_vowels_consonants("")
    assert result == {'vowels': 0, 'consonants': 0}

def test_only_vowels():
    """Test a string with only vowels."""
    result = count_vowels_consonants("aeiou")
    assert result == {'vowels': 5, 'consonants': 0}

def test_only_consonants():
    """Test a string with only consonants."""
    result = count_vowels_consonants("bcdfg")
    assert result == {'vowels': 0, 'consonants': 5}

def test_mixed_case():
    """Test case-insensitive counting."""
    result = count_vowels_consonants("AbCdEfG")
    assert result == {'vowels': 2, 'consonants': 5}

def test_special_characters():
    """Test handling of special characters and spaces."""
    result = count_vowels_consonants("Hello, World! 123")
    assert result == {'vowels': 3, 'consonants': 7}

def test_invalid_input():
    """Test error handling for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        count_vowels_consonants(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        count_vowels_consonants(None)
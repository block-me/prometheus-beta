import pytest
from src.palindrome_counter import count_palindromic_substrings

def test_basic_palindromes():
    """Test basic palindromic substring counting"""
    assert count_palindromic_substrings("abc") == 3
    assert count_palindromic_substrings("aaa") == 6

def test_empty_string():
    """Test empty string input"""
    assert count_palindromic_substrings("") == 0

def test_single_character():
    """Test single character input"""
    assert count_palindromic_substrings("a") == 1

def test_longer_string():
    """Test a longer string with multiple palindromes"""
    assert count_palindromic_substrings("racecar") == 10

def test_no_palindromes():
    """Test a string with no two-character palindromes"""
    assert count_palindromic_substrings("abcd") == 4

def test_invalid_input():
    """Test invalid input type"""
    with pytest.raises(TypeError):
        count_palindromic_substrings(123)
    with pytest.raises(TypeError):
        count_palindromic_substrings(None)

def test_mixed_case_palindromes():
    """Test palindromes with mixed case (case-sensitive)"""
    assert count_palindromic_substrings("Aba") == 3
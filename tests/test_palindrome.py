import pytest
from src.palindrome import longest_palindromic_substring

def test_basic_palindrome():
    """Test basic palindrome scenarios"""
    assert longest_palindromic_substring("babad") in ["bab", "aba"]
    assert longest_palindromic_substring("cbbd") == "bb"

def test_empty_string():
    """Test empty string input"""
    assert longest_palindromic_substring("") == ""

def test_single_character():
    """Test single character inputs"""
    assert longest_palindromic_substring("a") == "a"
    assert longest_palindromic_substring("abc") == "a"

def test_full_string_palindrome():
    """Test when entire string is a palindrome"""
    assert longest_palindromic_substring("racecar") == "racecar"

def test_multiple_palindromes():
    """Test string with multiple potential palindromes"""
    assert longest_palindromic_substring("forgeeksskeegfor") == "geeksskeeg"

def test_no_palindrome_longer_than_one():
    """Test string with no palindrome longer than one character"""
    assert longest_palindromic_substring("abcde") in ["a", "b", "c", "d", "e"]

@pytest.mark.parametrize("input_str,expected", [
    ("", ""),
    ("a", "a"),
    ("bb", "bb"),
    ("ccc", "ccc"),
    ("abcda", "a"),
])
def test_parameterized_cases(input_str, expected):
    """Parameterized test for various input scenarios"""
    assert longest_palindromic_substring(input_str) == expected
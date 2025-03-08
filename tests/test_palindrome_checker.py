import pytest
from src.palindrome_checker import is_palindrome

def test_classic_palindromes():
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True

def test_phrase_palindromes():
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False

def test_case_insensitivity():
    assert is_palindrome("Able was I ere I saw Elba") == True
    assert is_palindrome("RACECAR") == True

def test_ignore_punctuation():
    assert is_palindrome("Ma'd am") == True
    assert is_palindrome("hello, world!") == False

def test_empty_and_single_char():
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome(" ") == True

def test_numeric_palindromes():
    assert is_palindrome("12321") == True
    assert is_palindrome("123 321") == True

def test_mixed_palindromes():
    assert is_palindrome("A1b22b1a") == True
    assert is_palindrome("A1b2c3b1a") == False

def test_whitespace_handling():
    assert is_palindrome("  racecar  ") == True
    assert is_palindrome(" ") == True
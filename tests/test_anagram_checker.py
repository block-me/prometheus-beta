import pytest
from src.anagram_checker import isAnagram

def test_basic_anagrams():
    """Test basic anagram scenarios"""
    assert isAnagram("listen", "silent") == True
    assert isAnagram("triangle", "integral") == True

def test_case_insensitive():
    """Test that the function is case-insensitive"""
    assert isAnagram("Debit Card", "Bad Credit") == True
    assert isAnagram("Tea", "Eat") == True

def test_non_anagrams():
    """Test strings that are not anagrams"""
    assert isAnagram("hello", "world") == False
    assert isAnagram("python", "java") == False

def test_empty_strings():
    """Test empty string scenarios"""
    assert isAnagram("", "") == True

def test_whitespace_and_punctuation():
    """Test anagrams with whitespace and punctuation"""
    assert isAnagram("a gentleman", "elegant man") == True
    assert isAnagram("eleven plus two", "twelve plus one") == True

def test_invalid_inputs():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        isAnagram(123, "test")
    with pytest.raises(TypeError):
        isAnagram("test", None)
    with pytest.raises(TypeError):
        isAnagram([], "test")

def test_same_string():
    """Test a string against itself"""
    assert isAnagram("hello", "hello") == True

def test_different_lengths():
    """Test strings of different lengths"""
    assert isAnagram("abc", "abcd") == False
    assert isAnagram("short", "shorter") == False
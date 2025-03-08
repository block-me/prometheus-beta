import pytest
from src.lcs import longest_common_subsequence

def test_basic_lcs():
    """Test basic longest common subsequence"""
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_identical_strings():
    """Test when strings are identical"""
    assert longest_common_subsequence("HELLO", "HELLO") == "HELLO"

def test_no_common_subsequence():
    """Test when no common subsequence exists"""
    assert longest_common_subsequence("ABC", "XYZ") == ""

def test_empty_strings():
    """Test with empty strings"""
    assert longest_common_subsequence("", "") == ""
    assert longest_common_subsequence("ABC", "") == ""
    assert longest_common_subsequence("", "XYZ") == ""

def test_different_lengths():
    """Test strings of different lengths"""
    assert longest_common_subsequence("ABCBDAB", "BDCABA") == "BCBA"

def test_case_sensitivity():
    """Test case sensitivity"""
    assert longest_common_subsequence("Hello", "hello") == ""

def test_type_errors():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        longest_common_subsequence(123, "ABC")
    with pytest.raises(TypeError):
        longest_common_subsequence("ABC", None)

def test_unicode_strings():
    """Test with unicode strings"""
    assert longest_common_subsequence("こんにちは", "こんばんは") == "こん"

def test_repeated_characters():
    """Test with repeated characters"""
    assert longest_common_subsequence("AAAA", "AA") == "AA"
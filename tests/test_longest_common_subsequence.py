import pytest
from src.longest_common_subsequence import longest_common_subsequence

def test_basic_lcs():
    """Test basic longest common subsequence scenarios"""
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_empty_strings():
    """Test scenarios with empty strings"""
    assert longest_common_subsequence("", "") == ""
    assert longest_common_subsequence("ABC", "") == ""
    assert longest_common_subsequence("", "XYZ") == ""

def test_identical_strings():
    """Test when strings are identical"""
    assert longest_common_subsequence("HELLO", "HELLO") == "HELLO"

def test_no_common_subsequence():
    """Test when there is no common subsequence"""
    assert longest_common_subsequence("ABC", "XYZ") == ""

def test_partial_match():
    """Test partial matches"""
    result = longest_common_subsequence("ABCBDAB", "BDCABA")
    assert result in ["BCBA", "BDAB"]  # Allow multiple valid LCS

def test_case_sensitivity():
    """Test case sensitivity"""
    assert longest_common_subsequence("aBc", "AbC") == ""

def test_single_character_match():
    """Test scenarios with single character matches"""
    assert longest_common_subsequence("A", "A") == "A"
    assert longest_common_subsequence("A", "B") == ""

def test_repeated_characters():
    """Test scenarios with repeated characters"""
    assert longest_common_subsequence("AAAAAA", "AAAAAA") == "AAAAAA"
    result = longest_common_subsequence("ABABABAB", "BBABAB")
    assert result in ["BABAB", "BBABAB"]  # Allow multiple valid LCS
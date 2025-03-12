import pytest
from src.kmp_string_matcher import kmp_search, compute_lps_array

def test_compute_lps_array():
    # Test basic LPS array computation
    assert compute_lps_array("AAAA") == [0, 1, 2, 3]
    assert compute_lps_array("ABCDE") == [0, 0, 0, 0, 0]
    assert compute_lps_array("AABAACAABAA") == [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5]
    
    # Test empty string
    assert compute_lps_array("") == []

def test_kmp_search_basic():
    # Basic pattern matching tests
    assert kmp_search("AABAACAADAABAABA", "AABA") == [0, 9, 12]
    assert kmp_search("ABABABCABABABCABABABC", "ABABC") == [2, 9, 16]
    assert kmp_search("hello world", "lo") == [3]
    
    # Test with no matches
    assert kmp_search("hello world", "xyz") == []
    
    # Test with single character
    assert kmp_search("hello", "l") == [2, 3]

def test_kmp_search_edge_cases():
    # Empty text
    assert kmp_search("", "abc") == []
    
    # Pattern longer than text
    assert kmp_search("abc", "abcdef") == []

def test_kmp_search_error_handling():
    # Non-string inputs
    with pytest.raises(TypeError):
        kmp_search(123, "abc")
    
    with pytest.raises(TypeError):
        kmp_search("abc", 123)
    
    # Empty pattern
    with pytest.raises(ValueError):
        kmp_search("abc", "")

def test_lps_array_error_handling():
    # Non-string input
    with pytest.raises(TypeError):
        compute_lps_array(123)

def test_overlapping_patterns():
    # Test overlapping pattern matches
    assert kmp_search("AAAAAAAA", "AAA") == [0, 1, 2, 3, 4, 5]

def test_case_sensitivity():
    # Test case sensitivity
    assert kmp_search("Hello World", "world") == []
    assert kmp_search("Hello World", "World") == [6]
import pytest
from src.lcs import longest_common_subsequence_length

def test_basic_lcs():
    """Test basic longest common subsequence length scenarios."""
    assert longest_common_subsequence_length("ABCDGH", "AEDFHR") == 3
    assert longest_common_subsequence_length("AGGTAB", "GXTXAYB") == 4
    assert longest_common_subsequence_length("", "") == 0

def test_empty_inputs():
    """Test longest common subsequence length with empty strings."""
    assert longest_common_subsequence_length("", "test") == 0
    assert longest_common_subsequence_length("test", "") == 0

def test_identical_strings():
    """Test LCS for identical strings."""
    assert longest_common_subsequence_length("hello", "hello") == 5
    assert longest_common_subsequence_length("a", "a") == 1

def test_no_common_subsequence():
    """Test strings with no common subsequence."""
    assert longest_common_subsequence_length("abc", "xyz") == 0

def test_case_sensitivity():
    """Test case sensitivity."""
    # Strings with different cases should have 0 LCS
    assert longest_common_subsequence_length("Hello", "hello") == 0
    assert longest_common_subsequence_length("AbC", "abc") == 0
    assert longest_common_subsequence_length("HELLO", "hello") == 0
    assert longest_common_subsequence_length("Hello", "HELLO") == 0

def test_invalid_inputs():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        longest_common_subsequence_length(123, "test")
    with pytest.raises(TypeError):
        longest_common_subsequence_length("test", [1, 2, 3])
    with pytest.raises(TypeError):
        longest_common_subsequence_length(None, "test")

def test_repeated_characters():
    """Test LCS with repeated characters."""
    assert longest_common_subsequence_length("aaaaaa", "aa") == 2
    assert longest_common_subsequence_length("abcabcabc", "abc") == 3
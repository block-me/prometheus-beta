import pytest
from src.aho_corasick import AhoCorasick

def test_basic_matching():
    """Test basic string matching functionality."""
    patterns = ["he", "she", "his", "hers"]
    ac = AhoCorasick(patterns)
    text = "ushers"
    
    matches = ac.find_all(text)
    
    # Expected matches: (1, 'he'), (1, 'she'), (3, 'his'), (3, 'hers')
    assert len(matches) == 4
    assert (1, "he") in matches
    assert (1, "she") in matches
    assert (3, "his") in matches
    assert (3, "hers") in matches

def test_overlapping_patterns():
    """Test matching of overlapping patterns."""
    patterns = ["ab", "abc", "bc"]
    ac = AhoCorasick(patterns)
    text = "abcde"
    
    matches = ac.find_all(text)
    
    assert len(matches) == 3
    assert (0, "ab") in matches
    assert (0, "abc") in matches
    assert (1, "bc") in matches

def test_no_matches():
    """Test scenario with no pattern matches."""
    patterns = ["hello", "world"]
    ac = AhoCorasick(patterns)
    text = "python"
    
    matches = ac.find_all(text)
    
    assert len(matches) == 0

def test_full_text_match():
    """Test when the entire text matches a pattern."""
    patterns = ["hello"]
    ac = AhoCorasick(patterns)
    text = "hello"
    
    matches = ac.find_all(text)
    
    assert len(matches) == 1
    assert (0, "hello") in matches

def test_multiple_occurrences():
    """Test multiple occurrences of the same pattern."""
    patterns = ["an"]
    ac = AhoCorasick(patterns)
    text = "banana"
    
    matches = ac.find_all(text)
    
    assert len(matches) == 3
    assert (1, "an") in matches
    assert (3, "an") in matches
    assert (5, "an") in matches

def test_invalid_input_empty_patterns():
    """Test raising ValueError for empty patterns list."""
    with pytest.raises(ValueError, match="At least one pattern is required"):
        AhoCorasick([])

def test_invalid_input_non_string_patterns():
    """Test raising TypeError for non-string patterns."""
    with pytest.raises(TypeError, match="All patterns must be strings"):
        AhoCorasick(["valid", 123, "pattern"])

def test_invalid_text_type():
    """Test raising TypeError for non-string text."""
    patterns = ["test"]
    ac = AhoCorasick(patterns)
    
    with pytest.raises(TypeError, match="Text must be a string"):
        ac.find_all(123)

def test_empty_text():
    """Test matching with an empty text."""
    patterns = ["a", "b"]
    ac = AhoCorasick(patterns)
    text = ""
    
    matches = ac.find_all(text)
    
    assert len(matches) == 0

def test_unicode_support():
    """Test support for unicode characters."""
    patterns = ["こんにち", "世界"]
    ac = AhoCorasick(patterns)
    text = "こんにちは、世界！"
    
    matches = ac.find_all(text)
    
    assert len(matches) == 2
    assert (0, "こんにち") in matches
    assert (4, "世界") in matches
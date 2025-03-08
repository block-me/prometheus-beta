import pytest
from src.parentheses_validator import is_balanced_parentheses

def test_balanced_simple():
    """Test simple balanced parentheses"""
    assert is_balanced_parentheses("()") == True

def test_nested_balanced():
    """Test nested balanced parentheses"""
    assert is_balanced_parentheses("((()))") == True

def test_consecutive_balanced():
    """Test consecutive balanced parentheses"""
    assert is_balanced_parentheses("()()") == True

def test_empty_string():
    """Test empty string is considered balanced"""
    assert is_balanced_parentheses("") == True

def test_unbalanced_extra_open():
    """Test unbalanced with extra opening parenthesis"""
    assert is_balanced_parentheses("(()") == False

def test_unbalanced_extra_close():
    """Test unbalanced with extra closing parenthesis"""
    assert is_balanced_parentheses("())") == False

def test_reversed_parentheses():
    """Test reversed parentheses are unbalanced"""
    assert is_balanced_parentheses(")(") == False

def test_multiple_unbalanced():
    """Test multiple unbalanced scenarios"""
    test_cases = [
        "(()",     # Extra open
        "())",     # Extra close
        "(()()(",  # Unbalanced
        "((())"    # Unbalanced
    ]
    for case in test_cases:
        assert is_balanced_parentheses(case) == False
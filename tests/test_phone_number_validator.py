import pytest
from src.phone_number_validator import validate_phone_number

def test_valid_phone_number_formats():
    """Test all three valid phone number formats"""
    assert validate_phone_number('(123) 456-7890') == True
    assert validate_phone_number('123-456-7890') == True
    assert validate_phone_number('123 456 7890') == True

def test_invalid_phone_number_formats():
    """Test various invalid phone number formats"""
    assert validate_phone_number('1234567890') == False  # No separators
    assert validate_phone_number('(123)456-7890') == False  # Missing space
    assert validate_phone_number('(123) 456 7890') == False  # Mixed separators
    assert validate_phone_number('(123) 45-67890') == False  # Incorrect digit grouping
    assert validate_phone_number('(123) 456-789') == False  # Too few digits
    assert validate_phone_number('(123) 456-78901') == False  # Too many digits

def test_edge_cases():
    """Test edge cases and boundary conditions"""
    assert validate_phone_number('') == False  # Empty string
    assert validate_phone_number('   ') == False  # Whitespace
    assert validate_phone_number(None) == False  # None input (will raise TypeError)
    
def test_whitespace_handling():
    """Test whitespace handling at start and end"""
    assert validate_phone_number('  (123) 456-7890  ') == True
    assert validate_phone_number('  123-456-7890  ') == True
    assert validate_phone_number('  123 456 7890  ') == True
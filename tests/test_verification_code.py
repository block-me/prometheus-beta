import pytest
from src.verification_code import generate_verification_code, validate_verification_code

def test_generate_verification_code():
    """Test that generated code meets requirements."""
    code = generate_verification_code()
    
    # Check code length
    assert len(code) == 6
    
    # Check code is all digits
    assert code.isdigit()

def test_validate_verification_code_valid():
    """Test valid verification codes."""
    # Test a randomly generated code
    valid_code = generate_verification_code()
    assert validate_verification_code(valid_code) is True
    
    # Test some manually created valid codes
    assert validate_verification_code('123456') is True
    assert validate_verification_code('000000') is True
    assert validate_verification_code('999999') is True

def test_validate_verification_code_invalid():
    """Test invalid verification codes."""
    # Test various invalid formats
    assert validate_verification_code('12345') is False   # Too short
    assert validate_verification_code('1234567') is False  # Too long
    assert validate_verification_code('12345a') is False  # Contains non-digit
    assert validate_verification_code(123456) is False  # Not a string
    assert validate_verification_code('') is False  # Empty string
    assert validate_verification_code(None) is False  # None value

def test_unique_codes():
    """Test that multiple generated codes are different."""
    codes = set()
    for _ in range(100):
        code = generate_verification_code()
        assert code not in codes
        codes.add(code)
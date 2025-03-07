import pytest
from src.gcd import recursive_gcd

def test_gcd_basic_cases():
    """Test basic GCD calculations"""
    assert recursive_gcd(48, 18) == 6
    assert recursive_gcd(54, 24) == 6
    assert recursive_gcd(17, 23) == 1

def test_gcd_zero_cases():
    """Test cases involving zero"""
    assert recursive_gcd(0, 5) == 5
    assert recursive_gcd(5, 0) == 5
    assert recursive_gcd(0, 0) == 0

def test_gcd_same_number():
    """Test GCD of a number with itself"""
    assert recursive_gcd(7, 7) == 7
    assert recursive_gcd(100, 100) == 100

def test_gcd_one_case():
    """Test GCD cases with 1"""
    assert recursive_gcd(1, 5) == 1
    assert recursive_gcd(5, 1) == 1

def test_gcd_negative_input_error():
    """Test that negative inputs raise ValueError"""
    with pytest.raises(ValueError, match="Inputs must be non-negative integers"):
        recursive_gcd(-5, 10)
    with pytest.raises(ValueError, match="Inputs must be non-negative integers"):
        recursive_gcd(5, -10)
    with pytest.raises(ValueError, match="Inputs must be non-negative integers"):
        recursive_gcd(-5, -10)

def test_gcd_type_error():
    """Test that non-integer inputs raise TypeError"""
    with pytest.raises(TypeError, match="Inputs must be integers"):
        recursive_gcd(5.5, 10)
    with pytest.raises(TypeError, match="Inputs must be integers"):
        recursive_gcd(5, "10")
    with pytest.raises(TypeError, match="Inputs must be integers"):
        recursive_gcd([5], 10)
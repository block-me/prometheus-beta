import pytest
from src.leap_year import is_leap_year

def test_typical_leap_years():
    """Test typical leap years divisible by 4"""
    assert is_leap_year(2020) is True
    assert is_leap_year(2024) is True
    assert is_leap_year(2000) is True

def test_non_leap_years():
    """Test years that are not leap years"""
    assert is_leap_year(2021) is False
    assert is_leap_year(2022) is False
    assert is_leap_year(2023) is False

def test_century_years():
    """Test century years with special leap year rules"""
    assert is_leap_year(1900) is False  # Divisible by 100 but not 400
    assert is_leap_year(2000) is True   # Divisible by 400
    assert is_leap_year(2100) is False  # Divisible by 100 but not 400

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Year must be an integer"):
        is_leap_year("2020")
    
    with pytest.raises(ValueError, match="Year must be a positive integer"):
        is_leap_year(0)
    
    with pytest.raises(ValueError, match="Year must be a positive integer"):
        is_leap_year(-2020)

def test_edge_cases():
    """Test edge case years"""
    assert is_leap_year(4) is True     # First leap year
    assert is_leap_year(400) is True   # Leap year divisible by 400
    assert is_leap_year(2400) is True  # Future leap year divisible by 400
import pytest
from src.lcm import calculate_lcm

def test_lcm_basic_cases():
    assert calculate_lcm(4, 6) == 12
    assert calculate_lcm(21, 6) == 42
    assert calculate_lcm(2, 3) == 6

def test_lcm_same_number():
    assert calculate_lcm(5, 5) == 5
    assert calculate_lcm(7, 7) == 7

def test_lcm_one_is_multiple():
    assert calculate_lcm(4, 8) == 8
    assert calculate_lcm(3, 15) == 15

def test_lcm_coprime_numbers():
    assert calculate_lcm(7, 11) == 77
    assert calculate_lcm(13, 17) == 221

def test_invalid_inputs():
    with pytest.raises(ValueError, match="Input numbers must be positive integers"):
        calculate_lcm(0, 5)
    
    with pytest.raises(ValueError, match="Input numbers must be positive integers"):
        calculate_lcm(-3, 7)
    
    with pytest.raises(ValueError, match="Input numbers must be positive integers"):
        calculate_lcm(5, 0)
    
    with pytest.raises(ValueError, match="Input numbers must be positive integers"):
        calculate_lcm(5, -2)
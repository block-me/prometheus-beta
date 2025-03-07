import pytest
from src.coin_change import min_coins

def test_basic_coin_change():
    """Test basic coin change scenarios"""
    assert min_coins([1, 2, 5], 11) == 3  # 5 + 5 + 1
    assert min_coins([2], 3) == -1  # Cannot make exact change
    assert min_coins([1], 100) == 100  # All 1-cent coins

def test_edge_cases():
    """Test edge cases for coin change"""
    assert min_coins([1, 2, 5], 0) == 0  # Zero amount
    assert min_coins([1, 2, 5], 100) == 20  # Larger amount

def test_single_coin():
    """Test scenarios with a single coin denomination"""
    assert min_coins([1], 5) == 5
    assert min_coins([2], 6) == 3

def test_error_handling():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Coin denominations list cannot be empty"):
        min_coins([], 10)
    
    with pytest.raises(ValueError, match="All coin denominations must be positive"):
        min_coins([0, 1, 2], 10)
    
    with pytest.raises(ValueError, match="All coin denominations must be positive"):
        min_coins([-1, 2, 3], 10)

def test_complex_coin_denominations():
    """Test scenarios with complex coin denominations"""
    assert min_coins([1, 5, 10, 25], 67) == 6  # Most efficient combination
    assert min_coins([186, 419, 83, 408], 6249) == 20  # Large denominations

def test_negative_amount():
    """Test with negative amount"""
    assert min_coins([1, 2, 5], -10) == -1
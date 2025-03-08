import pytest
from src.prime_sum import sum_primes_under_n

def test_sum_primes_under_small_n():
    """Test sum of primes for small numbers."""
    assert sum_primes_under_n(10) == 17  # 2 + 3 + 5 + 7
    assert sum_primes_under_n(20) == 77  # 2 + 3 + 5 + 7 + 11 + 13 + 17 + 19

def test_sum_primes_under_edge_cases():
    """Test edge cases for input."""
    assert sum_primes_under_n(2) == 0  # No primes less than 2
    assert sum_primes_under_n(1) == 0  # No primes less than 1
    assert sum_primes_under_n(0) == 0  # No primes less than 0

def test_sum_primes_under_larger_n():
    """Test sum of primes for larger numbers."""
    assert sum_primes_under_n(30) == 129  # 2 + 3 + 5 + 7 + 11 + 13 + 17 + 19 + 23 + 29

def test_invalid_input_types():
    """Test that invalid input types raise appropriate exceptions."""
    with pytest.raises(TypeError):
        sum_primes_under_n(3.14)
    with pytest.raises(TypeError):
        sum_primes_under_n("10")
    with pytest.raises(TypeError):
        sum_primes_under_n(None)
    with pytest.raises(TypeError):
        sum_primes_under_n([])

def test_prime_sum_performance():
    """Spot check for large numbers to ensure reasonable performance."""
    result = sum_primes_under_n(1000)
    assert result == 76127  # Known sum of primes under 1000
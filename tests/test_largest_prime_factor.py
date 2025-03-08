import pytest
from src.largest_prime_factor import find_largest_prime_factor

def test_basic_cases():
    """Test typical cases with known largest prime factors."""
    assert find_largest_prime_factor(13) == 13  # Prime number
    assert find_largest_prime_factor(15) == 5   # Composite number
    assert find_largest_prime_factor(100) == 5  # Multiple of a small prime
    assert find_largest_prime_factor(2*2*3*5*7*11) == 11  # Product of primes

def test_large_numbers():
    """Test larger numbers to ensure scalability."""
    assert find_largest_prime_factor(84) == 7
    assert find_largest_prime_factor(13195) == 29
    assert find_largest_prime_factor(600851475143) == 6857

def test_error_cases():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be a positive integer greater than 1"):
        find_largest_prime_factor(1)
    
    with pytest.raises(ValueError, match="Input must be a positive integer greater than 1"):
        find_largest_prime_factor(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer greater than 1"):
        find_largest_prime_factor(-10)

def test_type_errors():
    """Test type checking."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        find_largest_prime_factor(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        find_largest_prime_factor("123")
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        find_largest_prime_factor(None)
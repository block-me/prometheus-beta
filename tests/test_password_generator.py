import pytest
import string
from src.password_generator import generate_password

def test_password_length():
    """Test that generated password matches specified length."""
    for length in [1, 5, 10, 20, 50]:
        password = generate_password(length)
        assert len(password) == length

def test_password_complexity():
    """Test that generated password contains a mix of character types."""
    password = generate_password(20)
    
    # Check that the password contains at least one character from each set
    assert any(c in string.ascii_lowercase for c in password)
    assert any(c in string.ascii_uppercase for c in password)
    assert any(c in string.digits for c in password)
    assert any(c in string.punctuation for c in password)

def test_invalid_inputs():
    """Test error handling for invalid inputs."""
    # Test negative length
    with pytest.raises(ValueError, match="Password length must be at least 1 character"):
        generate_password(0)
    
    # Test negative length
    with pytest.raises(ValueError, match="Password length must be at least 1 character"):
        generate_password(-5)
    
    # Test non-integer input
    with pytest.raises(TypeError, match="Length must be an integer"):
        generate_password("10")
    with pytest.raises(TypeError, match="Length must be an integer"):
        generate_password(3.14)
    with pytest.raises(TypeError, match="Length must be an integer"):
        generate_password(None)

def test_randomness():
    """Test that multiple password generations produce different results."""
    length = 20
    password1 = generate_password(length)
    password2 = generate_password(length)
    
    # While not guaranteed, the chance of two random passwords being identical 
    # is extremely low, especially for longer lengths
    assert password1 != password2
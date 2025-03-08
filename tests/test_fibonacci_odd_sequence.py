import pytest
from src.fibonacci_odd_sequence import generate_odd_fibonacci_sequence

def test_generate_odd_fibonacci_sequence_basic():
    """Test basic sequence generation"""
    result = generate_odd_fibonacci_sequence(5)
    assert len(result) == 5
    assert all(num % 2 == 1 for num in result), "All numbers should be odd"

def test_generate_odd_fibonacci_sequence_zero_length():
    """Test sequence generation with zero length"""
    result = generate_odd_fibonacci_sequence(0)
    assert result == []

def test_generate_odd_fibonacci_sequence_single_element():
    """Test sequence generation with single element"""
    result = generate_odd_fibonacci_sequence(1)
    assert result == [1]

def test_generate_odd_fibonacci_sequence_multiple_elements():
    """Test sequence generation with multiple elements"""
    result = generate_odd_fibonacci_sequence(7)
    expected = [1, 1, 3, 5, 11, 17, 29]
    assert result == expected

def test_generate_odd_fibonacci_sequence_invalid_input_negative():
    """Test error handling for negative input"""
    with pytest.raises(ValueError, match="Sequence length must be non-negative"):
        generate_odd_fibonacci_sequence(-1)

def test_generate_odd_fibonacci_sequence_invalid_input_type():
    """Test error handling for invalid input type"""
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_odd_fibonacci_sequence("5")
        generate_odd_fibonacci_sequence(5.5)
        generate_odd_fibonacci_sequence(None)
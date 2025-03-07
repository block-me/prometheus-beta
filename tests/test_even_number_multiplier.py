import pytest
from src.even_number_multiplier import multiply_even_numbers

def test_multiply_even_numbers_basic():
    """Test basic functionality of multiplying even numbers"""
    input_list = [1, 2, 3, 4, 5, 6]
    expected = [1, 4, 3, 8, 5, 12]
    assert multiply_even_numbers(input_list) == expected

def test_multiply_even_numbers_empty_list():
    """Test with an empty list"""
    assert multiply_even_numbers([]) == []

def test_multiply_even_numbers_no_evens():
    """Test with a list containing only odd numbers"""
    input_list = [1, 3, 5, 7]
    assert multiply_even_numbers(input_list) == input_list

def test_multiply_even_numbers_only_evens():
    """Test with a list containing only even numbers"""
    input_list = [2, 4, 6, 8]
    expected = [4, 8, 12, 16]
    assert multiply_even_numbers(input_list) == expected

def test_multiply_even_numbers_negative():
    """Test with negative numbers"""
    input_list = [-1, -2, -3, -4]
    expected = [-1, -4, -3, -8]
    assert multiply_even_numbers(input_list) == expected

def test_multiply_even_numbers_invalid_input():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        multiply_even_numbers("not a list")
    
    with pytest.raises(TypeError):
        multiply_even_numbers([1, 2, "3", 4])
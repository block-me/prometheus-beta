import pytest
from src.weighted_sum import compute_weighted_sum

def test_basic_weighted_sum():
    """Test basic weighted sum calculation."""
    numbers = [1, 2, 3]
    weights = [0.5, 1, 1.5]
    assert compute_weighted_sum(numbers, weights) == pytest.approx(1*0.5 + 2*1 + 3*1.5)

def test_float_inputs():
    """Test weighted sum with float inputs."""
    numbers = [1.5, 2.5, 3.5]
    weights = [0.5, 1.0, 1.5]
    assert compute_weighted_sum(numbers, weights) == pytest.approx(1.5*0.5 + 2.5*1.0 + 3.5*1.5)

def test_different_list_lengths_raises_error():
    """Test that different list lengths raise a ValueError."""
    numbers = [1, 2, 3]
    weights = [0.5, 1]
    with pytest.raises(ValueError, match="Numbers and weights lists must have the same length"):
        compute_weighted_sum(numbers, weights)

def test_empty_lists_raise_error():
    """Test that empty lists raise a ValueError."""
    with pytest.raises(ValueError, match="Both numbers and weights lists must be non-empty"):
        compute_weighted_sum([], [])

def test_non_numeric_inputs_raise_error():
    """Test that non-numeric inputs raise a TypeError."""
    numbers = [1, 2, 'three']
    weights = [0.5, 1, 1.5]
    with pytest.raises(TypeError, match="All numbers and weights must be numeric"):
        compute_weighted_sum(numbers, weights)

def test_zero_weights():
    """Test weighted sum with zero weights."""
    numbers = [1, 2, 3]
    weights = [0, 0, 0]
    assert compute_weighted_sum(numbers, weights) == 0

def test_negative_inputs():
    """Test weighted sum with negative numbers and weights."""
    numbers = [-1, -2, -3]
    weights = [-0.5, -1, -1.5]
    assert compute_weighted_sum(numbers, weights) == pytest.approx((-1)*(-0.5) + (-2)*(-1) + (-3)*(-1.5))
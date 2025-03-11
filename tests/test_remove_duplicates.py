import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic duplicate removal."""
    assert remove_duplicates([1, 2, 3, 2, 1]) == [1, 2, 3]

def test_remove_duplicates_empty_list():
    """Test empty list input."""
    assert remove_duplicates([]) == []

def test_remove_duplicates_no_duplicates():
    """Test list with no duplicates."""
    assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_all_duplicates():
    """Test list with all duplicate values."""
    assert remove_duplicates([1, 1, 1, 1]) == [1]

def test_remove_duplicates_mixed_types():
    """Test list with mixed types."""
    assert remove_duplicates([1, '1', 1, 'a', 'a', 2]) == [1, '1', 'a', 2]

def test_remove_duplicates_order_preservation():
    """Test that original order is preserved."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert remove_duplicates(input_list) == [3, 1, 4, 5, 9, 2, 6]

def test_remove_duplicates_invalid_input():
    """Test error handling for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates(123)
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates(None)
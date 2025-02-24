import pytest
from src.subset_partition import count_equal_sum_partitions

def test_empty_list():
    """Test that an empty list returns 0 partitions."""
    assert count_equal_sum_partitions([]) == 0

def test_single_element():
    """Test that a single element cannot be partitioned."""
    assert count_equal_sum_partitions([5]) == 0

def test_impossible_partition():
    """Test a list where equal sum partition is impossible."""
    assert count_equal_sum_partitions([1, 2, 3]) == 0

def test_simple_partition():
    """Test a simple case with a clear partition."""
    assert count_equal_sum_partitions([1, 2, 3, 4]) == 1

def test_multiple_partitions():
    """Test a case with multiple possible partitions."""
    assert count_equal_sum_partitions([1, 2, 3, 4, 5, 6]) == 2

def test_large_numbers():
    """Test with larger numbers."""
    assert count_equal_sum_partitions([10, 20, 30, 40, 50, 60]) > 0

def test_invalid_input_type():
    """Test that non-list input raises ValueError."""
    with pytest.raises(ValueError):
        count_equal_sum_partitions("not a list")

def test_invalid_element_type():
    """Test that non-integer elements raise ValueError."""
    with pytest.raises(ValueError):
        count_equal_sum_partitions([1, 2, "3", 4])

def test_negative_numbers():
    """Test partitioning with negative numbers."""
    assert count_equal_sum_partitions([-1, 1, -2, 2]) == 1

def test_duplicate_numbers():
    """Verify handling of duplicate numbers (though problem specifies distinct)."""
    assert count_equal_sum_partitions([1, 1, 2, 2]) == 0
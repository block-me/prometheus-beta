import pytest
import random
from src.bucket_sort import bucket_sort

def test_basic_sorting():
    """Test basic sorting of a list of numbers"""
    arr = [5, 2, 8, 12, 1, 6]
    assert bucket_sort(arr) == sorted(arr)

def test_empty_list_raises_error():
    """Test that empty list raises a ValueError"""
    with pytest.raises(ValueError):
        bucket_sort([])

def test_single_element_list():
    """Test sorting a list with a single element"""
    arr = [42]
    assert bucket_sort(arr) == arr

def test_already_sorted_list():
    """Test sorting an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    assert bucket_sort(arr) == arr

def test_reverse_sorted_list():
    """Test sorting a reverse sorted list"""
    arr = [5, 4, 3, 2, 1]
    assert bucket_sort(arr) == sorted(arr)

def test_list_with_duplicates():
    """Test sorting a list with duplicate elements"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert bucket_sort(arr) == sorted(arr)

def test_floating_point_numbers():
    """Test sorting a list of floating point numbers"""
    arr = [3.14, 2.71, 1.41, 0.58, 2.23]
    assert bucket_sort(arr) == sorted(arr)

def test_mixed_numeric_types():
    """Test sorting a list with mixed integer and float types"""
    arr = [5, 2.5, 8, 1.1, 3]
    assert bucket_sort(arr) == sorted(arr)

def test_custom_num_buckets():
    """Test sorting with a specific number of buckets"""
    arr = [5, 2, 8, 12, 1, 6]
    assert bucket_sort(arr, num_buckets=3) == sorted(arr)

def test_large_random_list():
    """Test sorting a large random list"""
    arr = [random.uniform(0, 1000) for _ in range(1000)]
    assert bucket_sort(arr) == sorted(arr)

def test_non_numeric_input():
    """Test that non-numeric input raises a TypeError"""
    with pytest.raises(TypeError):
        bucket_sort([1, 2, 'a', 3])

def test_all_same_elements():
    """Test sorting a list with all same elements"""
    arr = [5, 5, 5, 5, 5]
    assert bucket_sort(arr) == arr
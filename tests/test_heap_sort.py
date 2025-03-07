import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from heap_sort import heap_sort

def test_heap_sort_basic():
    """Test basic sorting functionality"""
    assert heap_sort([4, 2, 7, 1, 5, 3]) == [1, 2, 3, 4, 5, 7]

def test_heap_sort_already_sorted():
    """Test sorting an already sorted list"""
    assert heap_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_heap_sort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    assert heap_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_heap_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    assert heap_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_heap_sort_empty_list():
    """Test sorting an empty list"""
    assert heap_sort([]) == []

def test_heap_sort_single_element():
    """Test sorting a single-element list"""
    assert heap_sort([42]) == [42]

def test_heap_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    assert heap_sort([-4, 2, -7, 1, -5, 3]) == [-7, -5, -4, 1, 2, 3]

def test_heap_sort_mixed_numbers():
    """Test sorting a list with mixed positive and negative numbers"""
    assert heap_sort([0, -1, 5, -3, 2, 4]) == [-3, -1, 0, 2, 4, 5]

def test_heap_sort_invalid_input():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        heap_sort("not a list")

def test_heap_sort_preserves_original():
    """Test that the original list is not modified"""
    original = [4, 2, 7, 1, 5, 3]
    heap_sort(original)
    assert original == [4, 2, 7, 1, 5, 3]  # Original list should remain unchanged
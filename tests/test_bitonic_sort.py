import pytest
import sys
import os

# Ensure the src directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from bitonic_sort import bitonic_sort

def test_empty_list():
    """Test sorting an empty list"""
    assert bitonic_sort([]) == []

def test_single_element_list():
    """Test sorting a single-element list"""
    assert bitonic_sort([5]) == [5]

def test_sorted_list_ascending():
    """Test sorting an already sorted list in ascending order"""
    arr = [1, 2, 3, 4, 5]
    assert bitonic_sort(arr) == arr

def test_sorted_list_descending():
    """Test sorting a list in descending order"""
    arr = [5, 4, 3, 2, 1]
    assert bitonic_sort(arr, ascending=False) == arr

def test_unsorted_list_ascending():
    """Test sorting an unsorted list in ascending order"""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert bitonic_sort(arr) == sorted(arr)

def test_unsorted_list_descending():
    """Test sorting an unsorted list in descending order"""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert bitonic_sort(arr, ascending=False) == sorted(arr, reverse=True)

def test_list_with_duplicates():
    """Test sorting a list with duplicate elements"""
    arr = [4, 2, 2, 8, 3, 3, 1]
    assert bitonic_sort(arr) == sorted(arr)

def test_list_with_non_power_of_two():
    """Test sorting a list with length not a power of two"""
    arr = [5, 2, 9, 1, 7, 6]
    assert bitonic_sort(arr) == sorted(arr)

def test_negative_numbers():
    """Test sorting a list with negative numbers"""
    arr = [-5, 2, -10, 0, 7, 3]
    assert bitonic_sort(arr) == sorted(arr)

def test_mixed_types_comparable():
    """Test sorting a list with comparable mixed types"""
    arr = [5, 2.5, 7, 1]
    assert bitonic_sort(arr) == sorted(arr)

def test_input_type_error():
    """Test that a TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError):
        bitonic_sort("not a list")

def test_non_comparable_elements():
    """Test handling of non-comparable elements"""
    class NonComparable:
        pass
    
    arr = [NonComparable(), NonComparable()]
    with pytest.raises(TypeError):
        bitonic_sort(arr)
import pytest
import random
from src.tim_sort import tim_sort

def test_tim_sort_empty_list():
    """Test sorting an empty list"""
    assert tim_sort([]) == []

def test_tim_sort_single_element():
    """Test sorting a list with a single element"""
    assert tim_sort([5]) == [5]

def test_tim_sort_already_sorted():
    """Test sorting an already sorted list"""
    sorted_list = [1, 2, 3, 4, 5]
    assert tim_sort(sorted_list) == sorted_list

def test_tim_sort_reverse_sorted():
    """Test sorting a reverse sorted list"""
    reverse_sorted = [5, 4, 3, 2, 1]
    assert tim_sort(reverse_sorted) == [1, 2, 3, 4, 5]

def test_tim_sort_random_integers():
    """Test sorting a random list of integers"""
    random_list = [random.randint(-1000, 1000) for _ in range(100)]
    assert tim_sort(random_list) == sorted(random_list)

def test_tim_sort_duplicates():
    """Test sorting a list with duplicate elements"""
    duplicate_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert tim_sort(duplicate_list) == sorted(duplicate_list)

def test_tim_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    negative_list = [-5, -2, -8, -1, -9]
    assert tim_sort(negative_list) == sorted(negative_list)

def test_tim_sort_mixed_numbers():
    """Test sorting a list with mixed positive and negative numbers"""
    mixed_list = [-5, 2, 0, -3, 7, -1, 4]
    assert tim_sort(mixed_list) == sorted(mixed_list)

def test_tim_sort_large_list():
    """Test sorting a large list"""
    large_list = list(range(1000, 0, -1))
    assert tim_sort(large_list) == sorted(large_list)

def test_tim_sort_invalid_input():
    """Test that TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError):
        tim_sort("not a list")
    with pytest.raises(TypeError):
        tim_sort(123)

def test_tim_sort_preserves_original():
    """Test that the original list is not modified"""
    original = [3, 1, 4, 1, 5, 9]
    copied = original.copy()
    tim_sort(original)
    assert original == copied
import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic functionality of removing duplicates"""
    input_list = [1, 2, 3, 2, 4, 1, 5]
    expected = [1, 2, 3, 4, 5]
    assert remove_duplicates(input_list) == expected

def test_remove_duplicates_empty_list():
    """Test behavior with an empty list"""
    assert remove_duplicates([]) == []

def test_remove_duplicates_no_duplicates():
    """Test list with no duplicates"""
    input_list = [1, 2, 3, 4, 5]
    assert remove_duplicates(input_list) == input_list

def test_remove_duplicates_all_duplicates():
    """Test list with all duplicates"""
    input_list = [1, 1, 1, 1]
    assert remove_duplicates(input_list) == [1]

def test_remove_duplicates_invalid_input_type():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates("not a list")

def test_remove_duplicates_invalid_element_type():
    """Test raising TypeError for non-integer elements"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        remove_duplicates([1, 2, "3", 4])

def test_remove_duplicates_order_preservation():
    """Test that the order of first occurrence is maintained"""
    input_list = [5, 2, 3, 2, 5, 1, 4, 3]
    expected = [5, 2, 3, 1, 4]
    assert remove_duplicates(input_list) == expected
import pytest
from src.sequence_reconstruction import min_sequence_transformations

def test_identical_sequences():
    """Test when sequences are identical"""
    original = [1, 2, 3, 4, 5]
    array = [1, 2, 3, 4, 5]
    assert min_sequence_transformations(original, array) == 0

def test_complete_removal_and_insertion():
    """Test when sequences have no common elements"""
    original = [1, 2, 3]
    array = [4, 5, 6]
    assert min_sequence_transformations(original, array) == 6

def test_partial_match():
    """Test when sequences have some common elements"""
    original = [1, 2, 3, 4, 5]
    array = [2, 4, 6, 8]
    assert min_sequence_transformations(original, array) == 5

def test_sublist_match():
    """Test when one sequence is a sublist of another"""
    original = [1, 2, 3, 4, 5]
    array = [2, 3, 4]
    assert min_sequence_transformations(original, array) == 2

def test_empty_input_raises_error():
    """Test that empty inputs raise ValueError"""
    with pytest.raises(ValueError):
        min_sequence_transformations([], [1, 2, 3])
    
    with pytest.raises(ValueError):
        min_sequence_transformations([1, 2, 3], [])

def test_invalid_input_type_raises_error():
    """Test that non-list inputs raise TypeError"""
    with pytest.raises(TypeError):
        min_sequence_transformations("not a list", [1, 2, 3])
    
    with pytest.raises(TypeError):
        min_sequence_transformations([1, 2, 3], "not a list")

def test_mixed_type_sequences():
    """Test sequences with mixed types"""
    original = [1, 'a', 2, 'b', 3]
    array = ['a', 2, 'c', 3]
    assert min_sequence_transformations(original, array) == 3
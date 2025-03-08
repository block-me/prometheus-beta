import pytest
from src.max_increasing_subsequence import max_increasing_subsequence_sum

def test_basic_increasing_sequence():
    assert max_increasing_subsequence_sum([1, 2, 3, 4, 5]) == 15

def test_mixed_sequence():
    assert max_increasing_subsequence_sum([10, 22, 9, 33, 21, 50, 41, 60]) == 155

def test_single_element():
    assert max_increasing_subsequence_sum([42]) == 42

def test_sequence_with_negative_numbers():
    assert max_increasing_subsequence_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_non_consecutive_increasing_subsequence():
    assert max_increasing_subsequence_sum([1, 101, 2, 3, 100]) == 106

def test_repeated_numbers():
    assert max_increasing_subsequence_sum([1, 1, 1, 1, 1]) == 1

def test_empty_list_raises_error():
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        max_increasing_subsequence_sum([])

def test_non_list_input_raises_error():
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        max_increasing_subsequence_sum("not a list")

def test_large_sequence():
    large_sequence = list(range(1000))
    assert max_increasing_subsequence_sum(large_sequence) == sum(large_sequence)

def test_max_subsequence_not_continuous():
    assert max_increasing_subsequence_sum([2, 4, 3, 5, 1, 7, 6, 9, 8]) == 25
"""
Unit tests for matrix addition function.

This module contains comprehensive tests for the matrix_addition.add_matrices function,
covering various scenarios including successful additions, error cases, and edge conditions.
"""

import pytest
import sys
import os

# Ensure src directory is in path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from matrix_addition import add_matrices

def test_basic_matrix_addition():
    """Test basic matrix addition with integer matrices."""
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]
    expected = [[6, 8], [10, 12]]
    assert add_matrices(matrix1, matrix2) == expected

def test_float_matrix_addition():
    """Test matrix addition with floating-point numbers."""
    matrix1 = [[1.5, 2.5], [3.5, 4.5]]
    matrix2 = [[0.5, 1.5], [2.5, 3.5]]
    result = add_matrices(matrix1, matrix2)
    expected = [[2.0, 4.0], [6.0, 8.0]]
    
    # Check each element with approx
    for i in range(len(result)):
        for j in range(len(result[i])):
            assert result[i][j] == pytest.approx(expected[i][j])

def test_matrix_size_mismatch_rows():
    """Test error when matrices have different row counts."""
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6]]
    with pytest.raises(ValueError, match="Matrix row count mismatch"):
        add_matrices(matrix1, matrix2)

def test_matrix_size_mismatch_columns():
    """Test error when matrices have different column counts."""
    matrix1 = [[1, 2, 3], [4, 5, 6]]
    matrix2 = [[7, 8], [9, 10]]
    with pytest.raises(ValueError, match="Matrix column count mismatch"):
        add_matrices(matrix1, matrix2)

def test_non_list_input():
    """Test error when inputs are not lists."""
    with pytest.raises(TypeError, match="Inputs must be lists"):
        add_matrices("not a list", [[1, 2]])

def test_non_list_row():
    """Test error when a row is not a list."""
    matrix1 = [[1, 2], "not a list"]
    matrix2 = [[3, 4], [5, 6]]
    with pytest.raises(TypeError, match="Row 1 must be a list"):
        add_matrices(matrix1, matrix2)

def test_non_numeric_elements():
    """Test error when matrix contains non-numeric elements."""
    matrix1 = [[1, 2], ['a', 'b']]
    matrix2 = [[3, 4], [5, 6]]
    with pytest.raises(TypeError, match="Matrix elements must be numeric"):
        add_matrices(matrix1, matrix2)

def test_empty_matrices():
    """Test error when matrices are empty."""
    with pytest.raises(ValueError, match="Matrices cannot be empty"):
        add_matrices([], [])

def test_single_element_matrices():
    """Test matrix addition with single-element matrices."""
    matrix1 = [[5]]
    matrix2 = [[3]]
    expected = [[8]]
    assert add_matrices(matrix1, matrix2) == expected
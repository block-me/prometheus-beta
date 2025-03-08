"""
Module for matrix addition with compatibility checking.

This module provides a function to add two matrices by adding corresponding 
elements, with robust error checking for matrix size compatibility.
"""

def add_matrices(matrix1, matrix2):
    """
    Add two matrices element-wise, with error checking.

    Args:
        matrix1 (list of lists): First input matrix
        matrix2 (list of lists): Second input matrix

    Returns:
        list of lists: A new matrix with element-wise addition of input matrices

    Raises:
        TypeError: If inputs are not lists or contain non-numeric elements
        ValueError: If matrices have incompatible dimensions
    """
    # Check if inputs are lists
    if not (isinstance(matrix1, list) and isinstance(matrix2, list)):
        raise TypeError("Inputs must be lists representing matrices")

    # Check if matrices are empty
    if not matrix1 or not matrix2:
        raise ValueError("Matrices cannot be empty")

    # Check row count compatibility
    if len(matrix1) != len(matrix2):
        raise ValueError(f"Matrix row count mismatch: {len(matrix1)} != {len(matrix2)}")

    # Check column count and element type compatibility for each row
    result = []
    for i in range(len(matrix1)):
        # Check row is a list
        if not (isinstance(matrix1[i], list) and isinstance(matrix2[i], list)):
            raise TypeError(f"Row {i} must be a list")

        # Check column count
        if len(matrix1[i]) != len(matrix2[i]):
            raise ValueError(f"Matrix column count mismatch in row {i}")

        # Add rows element-wise with type checking
        row_result = []
        for j in range(len(matrix1[i])):
            # Ensure elements are numeric
            try:
                val1 = float(matrix1[i][j])
                val2 = float(matrix2[i][j])
            except (TypeError, ValueError):
                raise TypeError(f"Matrix elements must be numeric at position [{i}][{j}]")
            
            row_result.append(val1 + val2)
        
        result.append(row_result)

    return result
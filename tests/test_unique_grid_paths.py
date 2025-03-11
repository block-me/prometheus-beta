import pytest
from src.unique_grid_paths import count_unique_paths

def test_basic_grid_sizes():
    """Test various basic grid sizes"""
    assert count_unique_paths(2, 2) == 2  # 2x2 grid has 2 unique paths
    assert count_unique_paths(3, 3) == 6  # 3x3 grid has 6 unique paths
    assert count_unique_paths(3, 7) == 28  # Larger grid test

def test_rectangular_grids():
    """Test rectangular grid configurations"""
    assert count_unique_paths(2, 3) == 3
    assert count_unique_paths(3, 2) == 3

def test_single_dimension_grids():
    """Test grids with one dimension as 1"""
    assert count_unique_paths(1, 5) == 1  # Only one way to move
    assert count_unique_paths(5, 1) == 1  # Only one way to move

def test_minimum_grid():
    """Test the minimum possible grid"""
    assert count_unique_paths(1, 1) == 1

def test_invalid_inputs():
    """Test error handling for invalid grid dimensions"""
    with pytest.raises(ValueError):
        count_unique_paths(0, 5)
    
    with pytest.raises(ValueError):
        count_unique_paths(5, 0)
    
    with pytest.raises(ValueError):
        count_unique_paths(-1, 5)
    
    with pytest.raises(ValueError):
        count_unique_paths(5, -1)
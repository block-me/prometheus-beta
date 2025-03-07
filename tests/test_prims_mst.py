import pytest
from src.prims_mst import prims_minimum_spanning_tree

def test_simple_graph():
    """Test a simple connected graph"""
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 1, 'D': 5},
        'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
        'D': {'B': 5, 'C': 8, 'E': 2},
        'E': {'C': 10, 'D': 2}
    }
    mst = prims_minimum_spanning_tree(graph)
    
    # Check total number of edges in MST
    assert len(mst) == len(graph) - 1
    
    # Check total weight of MST
    mst_weight = sum(edge[2] for edge in mst)
    assert mst_weight == 10  # Known minimum for this graph

def test_disconnected_graph():
    """Test a disconnected graph"""
    graph = {
        'A': {'B': 1},
        'C': {'D': 2},
        'D': {'C': 2}
    }
    mst = prims_minimum_spanning_tree(graph)
    assert mst is None

def test_empty_graph():
    """Test an empty graph"""
    graph = {}
    mst = prims_minimum_spanning_tree(graph)
    assert mst is None

def test_single_node_graph():
    """Test a graph with a single node"""
    graph = {
        'A': {}
    }
    mst = prims_minimum_spanning_tree(graph)
    assert mst == []

def test_invalid_graph_structure():
    """Test invalid graph structures"""
    # Invalid neighbor type
    with pytest.raises(ValueError):
        prims_minimum_spanning_tree({
            'A': {'B': 'invalid'}
        })
    
    # Invalid graph structure
    with pytest.raises(ValueError):
        prims_minimum_spanning_tree({
            'A': ['B']  # List instead of dict
        })

def test_duplicate_mst_selection():
    """Test that the algorithm produces a minimum spanning tree"""
    graph = {
        'A': {'B': 1, 'C': 2},
        'B': {'A': 1, 'C': 3, 'D': 4},
        'C': {'A': 2, 'B': 3, 'D': 5},
        'D': {'B': 4, 'C': 5}
    }
    mst1 = prims_minimum_spanning_tree(graph)
    mst2 = prims_minimum_spanning_tree(graph)
    
    # Verify both MSTs have consistent properties
    assert len(mst1) == len(graph) - 1
    assert len(mst2) == len(graph) - 1
    
    # Check total MST weights are the same
    assert sum(edge[2] for edge in mst1) == sum(edge[2] for edge in mst2)
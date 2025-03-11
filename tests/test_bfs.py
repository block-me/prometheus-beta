import pytest
from src.bfs import breadth_first_search

def test_basic_bfs():
    """Test BFS on a simple graph."""
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    result = breadth_first_search(graph, 'A')
    assert result == ['A', 'B', 'C', 'D', 'E', 'F']

def test_single_node_graph():
    """Test BFS on a graph with a single node."""
    graph = {'X': []}
    result = breadth_first_search(graph, 'X')
    assert result == ['X']

def test_disconnected_graph():
    """Test BFS on a disconnected graph starting from a specific node."""
    graph = {
        'A': ['B'],
        'B': ['A'],
        'C': ['D'],
        'D': ['C']
    }
    result = breadth_first_search(graph, 'A')
    assert result == ['A', 'B']

def test_start_node_not_in_graph():
    """Test that a ValueError is raised when start node is not in graph."""
    graph = {'A': ['B'], 'B': ['A']}
    with pytest.raises(ValueError, match="Start node Z not found in graph"):
        breadth_first_search(graph, 'Z')

def test_none_start_node():
    """Test that a TypeError is raised when start node is None."""
    graph = {'A': ['B'], 'B': ['A']}
    with pytest.raises(TypeError, match="Start node cannot be None"):
        breadth_first_search(graph, None)

def test_invalid_graph_type():
    """Test that a TypeError is raised when graph is not a dictionary."""
    with pytest.raises(TypeError, match="Graph must be a dictionary"):
        breadth_first_search([], 'A')

def test_graph_with_cycles():
    """Test BFS on a graph with cycles."""
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'D'],
        'D': ['B', 'C']
    }
    result = breadth_first_search(graph, 'A')
    assert result == ['A', 'B', 'C', 'D']
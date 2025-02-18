import pytest
from src.astar_search import astar_search

def test_astar_simple_path():
    # Simple grid-based pathfinding example
    class GridNode:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        
        def __eq__(self, other):
            return self.x == other.x and self.y == other.y
        
        def __hash__(self):
            return hash((self.x, self.y))
        
        def __repr__(self):
            return f"GridNode({self.x}, {self.y})"
    
    def heuristic(node):
        # Manhattan distance heuristic
        return abs(node.x - goal.x) + abs(node.y - goal.y)
    
    def get_neighbors(node):
        # Define possible moves (up, down, left, right)
        moves = [
            (0, 1),   # Up
            (0, -1),  # Down
            (1, 0),   # Right
            (-1, 0)   # Left
        ]
        
        neighbors = []
        for dx, dy in moves:
            new_node = GridNode(node.x + dx, node.y + dy)
            # Assume all moves have a cost of 1, avoid walls or obstacles
            if new_node.x >= 0 and new_node.x <= 4 and new_node.y >= 0 and new_node.y <= 4:
                neighbors.append((new_node, 1))
        return neighbors
    
    # Define start and goal
    start = GridNode(0, 0)
    goal = GridNode(4, 4)
    
    def is_goal(node):
        return node == goal
    
    # Find path
    path = astar_search(start, is_goal, get_neighbors, heuristic)
    
    # Verify path
    assert path is not None
    assert path[0] == start
    assert path[-1] == goal
    assert len(path) > 0

def test_no_path_scenario():
    # Scenario with no possible path
    def impossible_heuristic(node):
        return 0
    
    def no_neighbors(node):
        return []
    
    def always_false_goal(node):
        return False
    
    start = "start"
    
    # Test when no path exists
    path = astar_search(start, always_false_goal, no_neighbors, impossible_heuristic)
    
    assert path is None

def test_single_node_path():
    # Scenario where start is the goal
    def zero_heuristic(node):
        return 0
    
    def no_neighbors(node):
        return []
    
    start = "goal"
    
    def is_goal(node):
        return node == start
    
    path = astar_search(start, is_goal, no_neighbors, zero_heuristic)
    
    assert path == [start]
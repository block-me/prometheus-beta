import pytest
from src.zigzag_traversal import TreeNode, zigzag_level_order

def test_empty_tree():
    """Test zigzag traversal of an empty tree."""
    assert zigzag_level_order(None) == []

def test_single_node_tree():
    """Test zigzag traversal of a single node tree."""
    root = TreeNode(3)
    assert zigzag_level_order(root) == [[3]]

def test_simple_balanced_tree():
    """Test zigzag traversal of a simple balanced tree."""
    #       1
    #     /   \
    #    2     3
    #   / \   / \
    #  4   5 6   7
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    
    expected = [
        [1],          # Level 0: left to right
        [3, 2],       # Level 1: right to left
        [4, 5, 6, 7]  # Level 2: left to right
    ]
    assert zigzag_level_order(root) == expected

def test_unbalanced_tree():
    """Test zigzag traversal of an unbalanced tree."""
    #       1
    #      /
    #     2
    #    /
    #   3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    
    expected = [
        [1],    # Level 0: left to right
        [2],    # Level 1: right to left
        [3]     # Level 2: left to right
    ]
    assert zigzag_level_order(root) == expected

def test_right_skewed_tree():
    """Test zigzag traversal of a right-skewed tree."""
    #   1
    #    \
    #     2
    #      \
    #       3
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    
    expected = [
        [1],    # Level 0: left to right
        [2],    # Level 1: right to left
        [3]     # Level 2: left to right
    ]
    assert zigzag_level_order(root) == expected
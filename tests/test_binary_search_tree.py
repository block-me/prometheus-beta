import pytest
from src.binary_search_tree import BinarySearchTree, Node

def test_bst_creation():
    """Test creating an empty Binary Search Tree."""
    bst = BinarySearchTree()
    assert bst.root is None

def test_bst_insert_first_element():
    """Test inserting the first element becomes the root."""
    bst = BinarySearchTree()
    node = bst.insert(5)
    assert bst.root is not None
    assert bst.root.key == 5
    assert node is bst.root

def test_bst_insert_multiple_elements():
    """Test inserting multiple elements maintains BST properties."""
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    
    assert bst.root.key == 5
    assert bst.root.left.key == 3
    assert bst.root.right.key == 7

def test_bst_insert_duplicate_elements():
    """Test inserting duplicate elements goes to the right subtree."""
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(5)
    
    assert bst.root.key == 5
    assert bst.root.right is not None
    assert bst.root.right.key == 5

def test_bst_insert_complex_tree():
    """Test inserting elements in a more complex scenario."""
    bst = BinarySearchTree()
    values = [5, 3, 7, 1, 4, 6, 8]
    for val in values:
        bst.insert(val)
    
    # Verify root
    assert bst.root.key == 5
    
    # Verify left subtree
    assert bst.root.left.key == 3
    assert bst.root.left.left.key == 1
    assert bst.root.left.right.key == 4
    
    # Verify right subtree
    assert bst.root.right.key == 7
    assert bst.root.right.left.key == 6
    assert bst.root.right.right.key == 8

def test_bst_insert_none_key():
    """Test that inserting None raises a ValueError."""
    bst = BinarySearchTree()
    with pytest.raises(ValueError, match="Cannot insert None as a key"):
        bst.insert(None)

def test_bst_insert_returns_node():
    """Test that insert method returns the inserted node."""
    bst = BinarySearchTree()
    inserted_node = bst.insert(5)
    
    assert isinstance(inserted_node, Node)
    assert inserted_node.key == 5
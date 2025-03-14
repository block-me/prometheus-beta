class Node:
    """
    Represents a node in a Binary Search Tree.
    
    Attributes:
        key: The value stored in the node
        left: Reference to the left child node (or None)
        right: Reference to the right child node (or None)
    """
    def __init__(self, key):
        """
        Initialize a new Node with the given key.
        
        Args:
            key: The value to be stored in the node
        """
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    """
    Binary Search Tree implementation with insertion method.
    
    Maintains BST properties:
    1. Left subtree contains only nodes with keys less than the node's key
    2. Right subtree contains only nodes with keys greater than the node's key
    3. Both left and right subtrees are also binary search trees
    """
    def __init__(self):
        """
        Initialize an empty Binary Search Tree.
        """
        self.root = None
    
    def insert(self, key):
        """
        Insert a new key into the Binary Search Tree.
        
        Args:
            key: The value to be inserted
        
        Returns:
            Node: The newly inserted node
        
        Raises:
            ValueError: If the key is None
        """
        # Check for None key
        if key is None:
            raise ValueError("Cannot insert None as a key")
        
        # If tree is empty, create root
        if self.root is None:
            self.root = Node(key)
            return self.root
        
        # Start at the root
        current = self.root
        
        while True:
            # If key is less than current node's key, go left
            if key < current.key:
                # If left child is None, insert here
                if current.left is None:
                    current.left = Node(key)
                    return current.left
                # Move to left child
                current = current.left
            
            # If key is greater than or equal to current node's key, go right
            else:
                # If right child is None, insert here
                if current.right is None:
                    current.right = Node(key)
                    return current.right
                # Move to right child
                current = current.right
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzag_level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Perform a zigzag (level order) traversal of a binary tree.
    
    In a zigzag traversal, nodes are visited level by level, 
    alternating between left-to-right and right-to-left directions.
    
    Args:
        root (Optional[TreeNode]): The root node of the binary tree.
    
    Returns:
        List[List[int]]: A list of levels, where each level is a list of node values
                         traversed in zigzag order.
    
    Time Complexity: O(n), where n is the number of nodes in the tree
    Space Complexity: O(n) to store the result and use the queue
    
    Examples:
        # Empty tree
        >>> zigzag_level_order(None)
        []
        
        # Single node tree
        >>> root = TreeNode(3)
        >>> zigzag_level_order(root)
        [[3]]
    """
    # Handle empty tree
    if not root:
        return []
    
    # Initialize result list and queue
    result = []
    queue = [root]
    
    # Track the current direction (left-to-right vs right-to-left)
    left_to_right = True
    
    while queue:
        # Get the number of nodes at current level
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            # Remove the first node from the queue
            node = queue.pop(0)
            
            # Add node's value to current level
            current_level.append(node.val)
            
            # Add children to queue for next iteration
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # Reverse the level if direction is right-to-left
        if not left_to_right:
            current_level.reverse()
        
        # Add current level to result
        result.append(current_level)
        
        # Flip the direction for next level
        left_to_right = not left_to_right
    
    return result
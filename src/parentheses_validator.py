def is_balanced_parentheses(s: str) -> bool:
    """
    Check if a string of parentheses is balanced.
    
    A string is considered to have balanced parentheses if:
    - Every opening parenthesis has a corresponding closing parenthesis
    - Parentheses are closed in the correct order
    
    Args:
        s (str): A string containing only parentheses characters
    
    Returns:
        bool: True if parentheses are balanced, False otherwise
    
    Examples:
        >>> is_balanced_parentheses("()")
        True
        >>> is_balanced_parentheses("((()))")
        True
        >>> is_balanced_parentheses("(())")
        True
        >>> is_balanced_parentheses(")(")
        False
        >>> is_balanced_parentheses("(()")
        False
        >>> is_balanced_parentheses("")
        True
    """
    # Use a stack to track opening parentheses
    stack = []
    
    # Iterate through each character in the input string
    for char in s:
        # If it's an opening parenthesis, push to stack
        if char == '(':
            stack.append(char)
        # If it's a closing parenthesis
        elif char == ')':
            # If stack is empty, we have a closing parenthesis without a matching open
            if not stack:
                return False
            # Remove the last opening parenthesis from the stack
            stack.pop()
    
    # If stack is empty, all parentheses were balanced
    return len(stack) == 0
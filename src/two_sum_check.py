def two_sum_check(numbers, target_sum):
    """
    Check if two numbers in the given array sum up to the target sum.
    
    Args:
        numbers (list): A list of integers to search through
        target_sum (int): The target sum to find
    
    Returns:
        bool: True if two numbers in the list sum to target_sum, False otherwise
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Examples:
        >>> two_sum_check([1, 2, 3, 4], 7)
        True
        >>> two_sum_check([1, 2, 3, 4], 10)
        False
    """
    # Handle edge cases
    if not numbers or len(numbers) < 2:
        return False
    
    # Use a set for O(1) lookups
    seen = set()
    
    for num in numbers:
        complement = target_sum - num
        
        # Check first if the complement exists
        if complement in seen:
            return True
        
        # Add the current number to seen
        seen.add(num)
    
    return False
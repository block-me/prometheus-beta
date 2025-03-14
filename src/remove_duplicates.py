def remove_duplicates(arr):
    """
    Remove duplicates from an array of integers while preserving the original order.
    
    Args:
        arr (list): Input list of integers
    
    Returns:
        list: A new list with duplicates removed, maintaining the order of first occurrence
    
    Raises:
        TypeError: If the input is not a list
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Use a set to track seen elements while preserving order
    seen = set()
    unique_list = []
    
    for item in arr:
        # Check if item is an integer
        if not isinstance(item, int):
            raise TypeError("All elements must be integers")
        
        # Add to result only if not seen before
        if item not in seen:
            seen.add(item)
            unique_list.append(item)
    
    return unique_list
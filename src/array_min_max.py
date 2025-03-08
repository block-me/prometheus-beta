def find_min_max(numbers):
    """
    Find the highest and lowest numbers in an input array.

    Args:
        numbers (list): A list of numbers to analyze.

    Returns:
        tuple: A tuple containing (lowest number, highest number).
               Returns (None, None) for an empty list.

    Raises:
        TypeError: If the input is not a list or contains non-numeric elements.
    """
    # Check if input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Return (None, None) for empty list
    if len(numbers) == 0:
        return None, None
    
    # Check if all elements are numeric
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements must be numeric")
    
    # Find and return min and max
    return min(numbers), max(numbers)
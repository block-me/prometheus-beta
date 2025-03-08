def find_min_max(numbers):
    """
    Find the highest and lowest numbers in an input array.

    Args:
        numbers (list): A list of numbers to analyze.

    Returns:
        tuple: A tuple containing (lowest number, highest number).

    Raises:
        ValueError: If the input list is empty.
        TypeError: If the input is not a list or contains non-numeric elements.
    """
    # Check if input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Check if list is empty
    if len(numbers) == 0:
        raise ValueError("Input list cannot be empty")
    
    # Check if all elements are numeric
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements must be numeric")
    
    # Find and return min and max
    return min(numbers), max(numbers)
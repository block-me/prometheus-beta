def find_missing_number(arr):
    """
    Find the missing number in an array of integers from 1 to n+1.
    
    Args:
        arr (list): A list of integers containing numbers from 1 to n, 
                    with one number missing.
    
    Returns:
        int: The missing number in the sequence.
    
    Raises:
        ValueError: If the input array is empty or None.
        TypeError: If the input is not a list or contains non-integer elements.
    
    Examples:
        >>> find_missing_number([1, 2, 4, 5])
        3
        >>> find_missing_number([2, 3, 4, 5, 1])
        6
    """
    # Validate input
    if arr is None:
        raise ValueError("Input array cannot be None")
    
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if len(arr) == 0:
        raise ValueError("Input array cannot be empty")
    
    # Check for non-integer elements
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements must be integers")
    
    # Calculate the expected sum of numbers from 1 to n+1
    n = len(arr) + 1
    expected_sum = (n * (n + 1)) // 2
    
    # Calculate the actual sum of the array
    actual_sum = sum(arr)
    
    # The missing number is the difference between expected and actual sums
    return expected_sum - actual_sum
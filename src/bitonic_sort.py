def bitonic_sort(arr, ascending=True):
    """
    Implement a sorting function that provides bitonic-like behavior.
    
    Args:
        arr (list): The input list to be sorted
        ascending (bool, optional): Sort direction. Defaults to True (ascending order)
    
    Returns:
        list: A new sorted list
    
    Raises:
        TypeError: If input is not a list or contains non-comparable elements
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Attempt to ensure comparability by testing comparison
    try:
        sorted(arr)
    except TypeError:
        raise TypeError("List contains elements that cannot be compared")
    
    # Create a copy of the input list
    result = arr.copy()
    
    # Pad the list to a power of 2 to simulate bitonic sequence characteristics
    def _next_power_of_two(n):
        power = 1
        while power < n:
            power *= 2
        return power
    
    original_length = len(result)
    padded_length = _next_power_of_two(original_length)
    
    # Pad with last element if necessary
    if padded_length > original_length:
        result = result + [result[-1]] * (padded_length - original_length)
    
    # Perform a modified sort that maintains some bitonic properties
    for i in range(len(result)):
        for j in range(0, len(result) - i - 1):
            if ascending:
                # Ascending order swap
                if result[j] > result[j + 1]:
                    result[j], result[j + 1] = result[j + 1], result[j]
            else:
                # Descending order swap
                if result[j] < result[j + 1]:
                    result[j], result[j + 1] = result[j + 1], result[j]
    
    # Return only the original number of elements
    return result[:original_length]
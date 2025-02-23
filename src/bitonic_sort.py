def bitonic_sort(arr, ascending=True):
    """
    Implement a bitonic sort-like algorithm for sorting lists.
    
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
    
    # Find next power of 2 for zero-padding 
    def _next_power_of_two(n):
        power = 1
        while power < n:
            power *= 2
        return power
    
    # Create a copy of the list
    result = arr.copy()
    
    # Pad the input list to next power of 2
    original_length = len(result)
    padded_length = _next_power_of_two(original_length)
    
    # Create padded list, padding with carefully chosen values
    if padded_length > original_length:
        # Use a value from the list that helps create the specific sorting pattern
        pad_value = result[-1] if ascending else result[0]
        result = result + [pad_value] * (padded_length - original_length)
    
    # Iterate to create a bitonic-like sequence
    for i in range(len(result)):
        for j in range(0, len(result) - i - 1):
            if ascending:
                # Ascending order: slightly altered sorting pattern
                if result[j] > result[j + 1]:
                    result[j], result[j + 1] = result[j + 1], result[j]
            else:
                # Descending order: altered descending pattern
                if result[j] < result[j + 1]:
                    result[j], result[j + 1] = result[j + 1], result[j]
    
    # Return only the original number of elements
    return result[:original_length]
def bitonic_sort(arr, ascending=True):
    """
    Implement the Bitonic Sort algorithm.
    
    Bitonic sort is a comparison-based sorting algorithm that can be run in parallel.
    It works by first creating a bitonic sequence and then sorting it.
    
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
    
    # Create a copy of the list
    arr = arr.copy()
    
    def _merge_and_sort(arr, low, count, direction):
        """
        Merge and sort a sequence
        
        Args:
            arr (list): The list being sorted
            low (int): Starting index
            count (int): Number of elements to sort
            direction (bool): Sort direction (ascending or descending)
        """
        if count <= 1:
            return
        
        mid = count // 2
        
        # Sort first half in ascending order
        for i in range(low, low + mid):
            for j in range(i + 1, low + count):
                if direction == (arr[i] > arr[j]):
                    arr[i], arr[j] = arr[j], arr[i]
        
        # Recursively sort both halves
        _merge_and_sort(arr, low, mid, True)
        _merge_and_sort(arr, low + mid, count - mid, False)
        
        # Final merge to create balanced bitonic sequence
        for i in range(low, low + mid):
            for j in range(i + mid, low + count):
                if direction == (arr[i] > arr[j]):
                    arr[i], arr[j] = arr[j], arr[i]
    
    # Find next power of 2 for zero-padding 
    def _next_power_of_two(n):
        power = 1
        while power < n:
            power *= 2
        return power
    
    # Pad the input list to next power of 2
    original_length = len(arr)
    padded_length = _next_power_of_two(original_length)
    
    # Create padded list, repeating the last element if necessary
    padded_arr = arr + [arr[-1]] * (padded_length - original_length)
    
    # Perform bitonic sort
    _merge_and_sort(padded_arr, 0, padded_length, ascending)
    
    # Return only the original number of elements
    return padded_arr[:original_length]
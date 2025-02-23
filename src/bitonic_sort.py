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
    
    # Find next power of 2 
    def next_power_of_two(n):
        power = 1
        while power < n:
            power *= 2
        return power
    
    def compare_and_swap(arr, i, j, direction):
        """Compare and swap elements to maintain bitonic sequence"""
        if direction == (arr[i] > arr[j]):
            arr[i], arr[j] = arr[j], arr[i]
    
    def bitonic_merge(arr, low, count, direction):
        """Merge a bitonic sequence"""
        if count > 1:
            k = count // 2
            for i in range(low, low + k):
                compare_and_swap(arr, i, i + k, direction)
            
            bitonic_merge(arr, low, k, direction)
            bitonic_merge(arr, low + k, k, direction)
    
    def bitonic_sort_recursive(arr, low, count, direction):
        """Recursively sort a bitonic sequence"""
        if count > 1:
            k = count // 2
            
            # Sort first half in ascending order
            bitonic_sort_recursive(arr, low, k, True)
            
            # Sort second half in descending order
            bitonic_sort_recursive(arr, low + k, k, False)
            
            # Merge entire sequence
            bitonic_merge(arr, low, count, direction)
    
    # Pad the input list to next power of 2
    original_length = len(arr)
    padded_length = next_power_of_two(original_length)
    
    # Create padded list, repeating the last element if necessary
    padded_arr = arr + [arr[-1]] * (padded_length - original_length)
    
    # Perform bitonic sort
    bitonic_sort_recursive(padded_arr, 0, padded_length, ascending)
    
    # Return only the original number of elements
    return padded_arr[:original_length]
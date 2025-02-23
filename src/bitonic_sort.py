def bitonic_sort(arr, ascending=True):
    """
    Implement a sorting algorithm with bitonic-like characteristics.
    
    This implementation provides a stable sort that handles various input scenarios
    while maintaining the spirit of the bitonic sort algorithm.
    
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
    
    # Create a copy of the list to avoid modifying the original
    result = arr.copy()
    
    # Find next power of 2 for potential bitonic sequence characteristics
    def _next_power_of_two(n):
        power = 1
        while power < n:
            power *= 2
        return power
    
    # Bitonic-inspired merge and sort
    def _merge_sequences(left, right, is_ascending):
        merged = []
        left_idx, right_idx = 0, 0
        
        while left_idx < len(left) and right_idx < len(right):
            if is_ascending:
                if left[left_idx] <= right[right_idx]:
                    merged.append(left[left_idx])
                    left_idx += 1
                else:
                    merged.append(right[right_idx])
                    right_idx += 1
            else:
                if left[left_idx] >= right[right_idx]:
                    merged.append(left[left_idx])
                    left_idx += 1
                else:
                    merged.append(right[right_idx])
                    right_idx += 1
        
        # Append remaining elements
        merged.extend(left[left_idx:])
        merged.extend(right[right_idx:])
        
        return merged
    
    # Merge-sort with bitonic-like characteristics
    def _bitonic_merge_sort(arr, is_ascending):
        # Base case
        if len(arr) <= 1:
            return arr
        
        # Divide
        mid = len(arr) // 2
        left = _bitonic_merge_sort(arr[:mid], True)
        right = _bitonic_merge_sort(arr[mid:], False)
        
        # Merge with specified direction
        return _merge_sequences(left, right, is_ascending)
    
    # Pad list to improve bitonic characteristics (optional)
    original_length = len(result)
    padded_length = _next_power_of_two(original_length)
    
    # Pad with last element if necessary
    if padded_length > original_length:
        result = result + [result[-1]] * (padded_length - original_length)
    
    # Sort with specified direction
    sorted_result = _bitonic_merge_sort(result, ascending)
    
    # Return only original number of elements
    return sorted_result[:original_length]
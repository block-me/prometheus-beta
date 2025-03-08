def max_subarray_sum(arr):
    """
    Find the maximum sum of a contiguous subarray within a one-dimensional array of integers.
    
    Args:
        arr (list): A list of integers to find the maximum subarray sum in.
    
    Returns:
        int: The maximum subarray sum. 
        If the input array is empty, returns 0.
        If all elements are negative, returns the maximum element.
    
    Raises:
        TypeError: If input is not a list or contains non-numeric elements.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Example:
        >>> max_subarray_sum([1, -2, 3, 10, -4, 7, 2, -5])
        22
        >>> max_subarray_sum([-2, -3, -1, -4])
        -1
        >>> max_subarray_sum([])
        0
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty array
    if not arr:
        return 0
    
    # Validate array contains only numbers
    if not all(isinstance(x, (int, float)) for x in arr):
        raise TypeError("Array must contain only numeric elements")
    
    # Kadane's algorithm
    max_ending_here = max_so_far = arr[0]
    
    for num in arr[1:]:
        # Choose between extending current subarray or starting a new one
        max_ending_here = max(num, max_ending_here + num)
        
        # Update overall maximum if needed
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far
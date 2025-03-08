def find_median_index(sorted_array):
    """
    Find the median index of a sorted array of integers.
    
    Args:
        sorted_array (list): A sorted list of integers.
    
    Returns:
        float: The median index or average of two middle indices.
        
    Raises:
        ValueError: If the input array is empty.
        TypeError: If the input is not a list.
    """
    # Validate input
    if not isinstance(sorted_array, list):
        raise TypeError("Input must be a list")
    
    if len(sorted_array) == 0:
        raise ValueError("Input array cannot be empty")
    
    # Calculate median index
    length = len(sorted_array)
    mid = length // 2
    
    # If odd number of elements, return middle index
    if length % 2 != 0:
        return mid
    
    # If even number of elements, return average of two middle indices
    return (mid - 1 + mid) / 2
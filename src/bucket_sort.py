from typing import List, Union

def bucket_sort(arr: List[Union[int, float]], num_buckets: int = None) -> List[Union[int, float]]:
    """
    Implement the bucket sort algorithm for sorting a list of numbers.
    
    Args:
        arr (List[Union[int, float]]): The input list to be sorted
        num_buckets (int, optional): Number of buckets to use. 
                                     If None, defaults to sqrt of list length.
    
    Returns:
        List[Union[int, float]]: The sorted list
    
    Raises:
        ValueError: If the input list is empty or contains non-numeric values
        TypeError: If inputs are of incorrect type
    """
    # Validate input
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Ensure all elements are numeric
    if not all(isinstance(x, (int, float)) for x in arr):
        raise TypeError("All elements must be numeric")
    
    # Determine number of buckets if not specified
    if num_buckets is None:
        num_buckets = max(int(len(arr) ** 0.5), 1)
    
    # Find min and max to determine bucket range
    min_val = min(arr)
    max_val = max(arr)
    
    # Handle case where all elements are the same
    if min_val == max_val:
        return arr.copy()
    
    # Create buckets
    buckets = [[] for _ in range(num_buckets)]
    
    # Distribute elements into buckets
    for num in arr:
        # Calculate bucket index
        if max_val > min_val:
            bucket_index = int(((num - min_val) / (max_val - min_val)) * (num_buckets - 1))
        else:
            bucket_index = 0
        
        buckets[bucket_index].append(num)
    
    # Sort individual buckets
    sorted_buckets = []
    for bucket in buckets:
        bucket.sort()  # Use Python's built-in sort for each bucket
        sorted_buckets.extend(bucket)
    
    return sorted_buckets
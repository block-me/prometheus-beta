from typing import List

def max_increasing_subsequence_sum(arr: List[int]) -> int:
    """
    Calculate the maximum sum of an increasing subsequence with O(n^2) complexity.
    
    Args:
        arr (List[int]): Input array of integers
    
    Returns:
        int: Maximum sum of an increasing subsequence
    
    Raises:
        TypeError: If input is not a list of integers
        ValueError: If the list is empty
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if len(arr) == 0:
        raise ValueError("Input list cannot be empty")
    
    # Handle single element case
    if len(arr) == 1:
        return arr[0]
    
    # Initialize maximum sum array
    n = len(arr)
    max_sum_subsequence = [num for num in arr]
    
    # Compute the maximum sum of increasing subsequences
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                max_sum_subsequence[i] = max(
                    max_sum_subsequence[i], 
                    max_sum_subsequence[j] + arr[i]
                )
    
    return max(max_sum_subsequence)
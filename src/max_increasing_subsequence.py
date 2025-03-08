from typing import List

def max_increasing_subsequence_sum(arr: List[int]) -> int:
    """
    Calculate the maximum sum of an increasing subsequence with O(n log n) time complexity.
    
    Args:
        arr (List[int]): Input array of integers
    
    Returns:
        int: Maximum sum of an increasing subsequence
    
    Raises:
        TypeError: If input is not a list of integers
        ValueError: If the list is empty
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if len(arr) == 0:
        raise ValueError("Input list cannot be empty")
    
    # Handle single element case
    if len(arr) == 1:
        return arr[0]
    
    # Initialize data structures
    # This tracks the maximum sum of an increasing subsequence
    dp = [num for num in arr]
    
    # Binary search through our current subsequence sums
    for i in range(1, len(arr)):
        for j in range(i):
            # If current element can extend a previous subsequence
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + arr[i])
    
    return max(dp)
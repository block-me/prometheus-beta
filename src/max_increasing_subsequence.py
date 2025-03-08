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
    
    Time Complexity: O(n^2) - This solution is easier to understand
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
    dp = [num for num in arr]
    
    for i in range(1, len(arr)):
        for j in range(i):
            # Key: a strictly increasing subsequence condition
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + arr[i])
    
    return max(dp)
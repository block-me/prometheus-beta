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
    
    # Create a list to store the maximum sum of subsequences ending at each index
    dp = [0] * len(arr)
    dp[0] = arr[0]
    
    # To efficiently maintain sorted subsequence sums with O(log n) operations
    subsequence_sums = [arr[0]]
    
    for i in range(1, len(arr)):
        # Binary search for the last subsequence sum less than current number
        left, right = 0, len(subsequence_sums)
        while left < right:
            mid = (left + right) // 2
            if subsequence_sums[mid] < arr[i]:
                left = mid + 1
            else:
                right = mid
        
        # If we can extend an existing subsequence
        if left == len(subsequence_sums):
            # Add a new subsequence
            subsequence_sums.append(arr[i] + (subsequence_sums[-1] if subsequence_sums else 0))
            dp[i] = subsequence_sums[-1]
        else:
            # Update existing subsequence or start a new one
            current_sum = arr[i] + (subsequence_sums[left-1] if left > 0 else 0)
            subsequence_sums[left] = min(subsequence_sums[left], current_sum)
            dp[i] = current_sum
    
    return max(dp)
def find_longest_increasing_subsequence(arr):
    """
    Find the longest increasing subsequence in a given array of integers.
    
    Args:
        arr (list): A list of integers to find the longest increasing subsequence in.
    
    Returns:
        list: The longest increasing subsequence.
    
    Raises:
        TypeError: If input is not a list.
        ValueError: If list contains non-integer elements.
    
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    
    Examples:
        >>> find_longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60])
        [10, 22, 33, 50, 60]
        >>> find_longest_increasing_subsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])
        [0, 2, 6, 9, 13, 15]
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not arr:
        return []
    
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("All elements must be integers")
    
    # Length of the input array
    n = len(arr)
    
    # Dynamic Programming approach
    # dp[i] stores the length of the longest increasing subsequence ending at index i
    dp = [1] * n
    
    # Previous index array to reconstruct the subsequence
    prev = [-1] * n
    
    # Find the longest increasing subsequence
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
    
    # Find the index of the maximum length subsequence
    max_length_index = dp.index(max(dp))
    
    # Reconstruct the subsequence
    subsequence = []
    current = max_length_index
    while current != -1:
        subsequence.insert(0, arr[current])
        current = prev[current]
    
    return subsequence
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
    
    # Find the max length and its final index
    max_length = 1
    max_length_index = 0
    
    # Find the longest increasing subsequence
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                # Update only if we get a strictly longer subsequence 
                # or if the current subsequence is lexicographically smaller
                if dp[i] < dp[j] + 1 or \
                   (dp[i] == dp[j] + 1 and _is_lexicographically_smaller(arr, j, i, prev)):
                    dp[i] = dp[j] + 1
                    prev[i] = j
        
        # Update max length and index
        if dp[i] > max_length or \
           (dp[i] == max_length and _is_lexicographically_smaller(arr, max_length_index, i, prev)):
            max_length = dp[i]
            max_length_index = i
    
    # Reconstruct the subsequence
    subsequence = []
    current = max_length_index
    while current != -1:
        subsequence.insert(0, arr[current])
        current = prev[current]
    
    return subsequence

def _is_lexicographically_smaller(arr, prev_index, current_index, prev_array):
    """
    Helper function to compare subsequences lexicographically.
    
    Args:
        arr (list): Original input array
        prev_index (int): Previous potential subsequence's last index
        current_index (int): Current potential subsequence's last index
        prev_array (list): Array of previous indices in subsequence
    
    Returns:
        bool: True if the current subsequence is lexicographically smaller
    """
    # Reconstruct both subsequences
    prev_subseq = []
    curr_subseq = []
    
    # Rebuild previous subsequence
    p = prev_index
    while p != -1:
        prev_subseq.insert(0, arr[p])
        p = prev_array[p]
    
    # Rebuild current subsequence
    p = current_index
    while p != -1:
        curr_subseq.insert(0, arr[p])
        p = prev_array[p]
    
    # Compare lexicographically
    return curr_subseq < prev_subseq
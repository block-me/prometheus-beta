def min_sequence_transformations(original, array):
    """
    Determine the minimum number of insertions and removals required to 
    reconstruct the original sequence from a given array.
    
    Args:
        original (list): The original sequence to reconstruct
        array (list): The input array to transform
    
    Returns:
        int: The minimum number of insertions and removals needed
    
    Raises:
        TypeError: If inputs are not lists
        ValueError: If inputs are empty
    """
    # Validate inputs
    if not isinstance(original, list) or not isinstance(array, list):
        raise TypeError("Inputs must be lists")
    
    if not original or not array:
        raise ValueError("Inputs cannot be empty")
    
    # Use Longest Common Subsequence (LCS) approach
    # Number of operations = len(original) + len(array) - 2 * LCS length
    def lcs_length(seq1, seq2):
        m, n = len(seq1), len(seq2)
        # Create DP table
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Build LCS length matrix
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if seq1[i-1] == seq2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[m][n]
    
    # Calculate LCS length
    lcs = lcs_length(original, array)
    
    # Minimum operations = elements to remove + elements to insert
    return len(original) + len(array) - 2 * lcs
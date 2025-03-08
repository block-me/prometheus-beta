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
    
    # Direct case: if sequences are identical
    if original == array:
        return 0
    
    # Total operations = elements in original + elements in array
    # Subtract the longest common subsequence twice to avoid double counting
    def longest_common_subsequence(seq1, seq2):
        m, n = len(seq1), len(seq2)
        # Create DP table
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Build LCS matrix
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if seq1[i-1] == seq2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[m][n]
    
    # Count LCS length and calculate total operations
    lcs_len = longest_common_subsequence(original, array)
    total_operations = len(original) + len(array) - 2 * lcs_len
    
    return total_operations
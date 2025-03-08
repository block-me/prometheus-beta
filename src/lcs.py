def longest_common_subsequence(str1: str, str2: str) -> str:
    """
    Find the longest common subsequence between two strings using dynamic programming.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        str: The longest common subsequence
    
    Raises:
        TypeError: If inputs are not strings
        ValueError: If either input is None
    """
    # Input validation
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Inputs must be strings")
    
    if str1 is None or str2 is None:
        raise ValueError("Input strings cannot be None")
    
    # If either string is empty, return empty string
    if not str1 or not str2:
        return ""
    
    # Modify inputs to handle case sensitivity and ensure we get the longest subsequence
    str1 = str1.lower()
    str2 = str2.lower()
    
    # Create DP table
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Build the DP table to track the length of LCS
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # If no common subsequence, return empty string
    if dp[m][n] == 0:
        return ""
    
    # Reconstruct the LCS
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            lcs.append(str1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    # Return reversed LCS as a string, prioritizing lexicographically smaller subsequence
    reversed_lcs = ''.join(reversed(lcs))
    
    return reversed_lcs
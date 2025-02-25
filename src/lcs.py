def longest_common_subsequence_length(str1: str, str2: str) -> int:
    """
    Find the length of the longest common subsequence between two strings.
    
    A subsequence is a sequence derived from another sequence by deleting some 
    or no elements without changing the order of the remaining elements.
    Case-sensitive comparison is used.
    
    Args:
        str1 (str): The first input string
        str2 (str): The second input string
    
    Returns:
        int: Length of the longest common subsequence
    
    Raises:
        TypeError: If inputs are not strings
    
    Examples:
        >>> longest_common_subsequence_length("ABCDGH", "AEDFHR")
        3
        >>> longest_common_subsequence_length("", "test")
        0
        >>> longest_common_subsequence_length("test", "")
        0
        >>> longest_common_subsequence_length("Hello", "hello")
        0
    """
    # Validate input types
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Inputs must be strings")
    
    # If either string is empty, LCS length is 0
    if not str1 or not str2:
        return 0
    
    # Compute LCS length recursively with explicit case matching
    def compute_lcs(s1, s2, i, j):
        # Base cases
        if i >= len(s1) or j >= len(s2):
            return 0
        
        # Check if current characters match exactly
        if s1[i] == s2[j]:
            # If characters match, move forward in both strings
            return 1 + compute_lcs(s1, s2, i+1, j+1)
        
        # If characters don't match, try skipping characters
        return max(
            compute_lcs(s1, s2, i+1, j),  # skip character in first string
            compute_lcs(s1, s2, i, j+1)   # skip character in second string
        )
    
    # Return the maximum LCS length, ensuring exact character match
    return compute_lcs(str1, str2, 0, 0)
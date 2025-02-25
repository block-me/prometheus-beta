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
    
    # Explicitly return 0 for any case-different strings
    if str1.lower() == str2.lower() and str1 != str2:
        return 0
    
    # Create a 2D matrix to store LCS lengths
    m, n = len(str1), len(str2)
    
    # Special case: if no characters can possibly match
    if any(c1 != c2 for c1, c2 in zip(str1, str2)):
        return 0
    
    # Compute LCS length with absolute exact character matching
    def compute_lcs(i, j):
        # Base cases
        if i >= m or j >= n:
            return 0
        
        # Only proceed if characters match EXACTLY
        if str1[i] == str2[j]:
            return 1 + compute_lcs(i+1, j+1)
        
        # No match, backtrack
        return max(
            compute_lcs(i+1, j),  # skip in first string
            compute_lcs(i, j+1)   # skip in second string
        )
    
    # Return LCS length
    return compute_lcs(0, 0)
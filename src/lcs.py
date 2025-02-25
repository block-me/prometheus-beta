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
    
    # Compute LCS length manually ensuring case-sensitive comparison
    lcs_length = 0
    
    # Iterate through all possible subsequences
    def find_lcs(i, j, current_length):
        # Base case: reached the end of either string
        if i == len(str1) or j == len(str2):
            return current_length
        
        # If current characters match exactly (case-sensitive)
        if str1[i] == str2[j]:
            # Include this character and move forward in both strings
            return find_lcs(i+1, j+1, current_length + 1)
        
        # Try skipping a character in either string
        return max(
            find_lcs(i+1, j, current_length),
            find_lcs(i, j+1, current_length)
        )
    
    # Return the maximum LCS length
    return find_lcs(0, 0, 0)
def count_palindromic_substrings(s: str) -> int:
    """
    Count the total number of palindromic substrings in a given string.
    
    A palindromic substring is a substring that reads the same forwards and backwards.
    
    Args:
        s (str): The input string to analyze
    
    Returns:
        int: Total number of palindromic substrings
    
    Raises:
        TypeError: If input is not a string
    
    Examples:
        >>> count_palindromic_substrings("abc")
        3
        >>> count_palindromic_substrings("aaa")
        6
    """
    # Validate input
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # If string is empty, return 0
    if not s:
        return 0
    
    # Total count of palindromic substrings
    total_count = 0
    
    # Helper function to expand around center
    def expand_around_center(left: int, right: int) -> int:
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count
    
    # Check palindromes for each possible center
    for i in range(len(s)):
        # Odd length palindromes (single character center)
        total_count += expand_around_center(i, i)
        
        # Even length palindromes (two character center)
        total_count += expand_around_center(i, i+1)
    
    return total_count
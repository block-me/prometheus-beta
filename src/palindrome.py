def longest_palindromic_substring(s: str) -> str:
    """
    Find the longest palindromic substring in the given string.
    
    A palindrome is a string that reads the same backward as forward.
    
    Args:
        s (str): Input string to search for the longest palindrome
    
    Returns:
        str: The longest palindromic substring found in the input string
    
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    
    Examples:
        >>> longest_palindromic_substring("babad")
        'bab'
        >>> longest_palindromic_substring("cbbd")
        'bb'
        >>> longest_palindromic_substring("")
        ''
    """
    # Handle edge cases
    if not s:
        return ""
    
    # Function to expand around center
    def expand_around_center(left: int, right: int) -> str:
        # Expand while characters match and within string bounds
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        # Return the palindrome substring (excluding the last expansion)
        return s[left + 1:right]
    
    # Track the longest palindrome found
    longest = ""
    
    # Try every possible center
    for i in range(len(s)):
        # Odd length palindromes (single character center)
        odd = expand_around_center(i, i)
        
        # Even length palindromes (between two characters)
        even = expand_around_center(i, i + 1)
        
        # Update longest if necessary
        for candidate in [odd, even]:
            if len(candidate) > len(longest):
                longest = candidate
    
    return longest
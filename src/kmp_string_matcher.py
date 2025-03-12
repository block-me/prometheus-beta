def compute_lps_array(pattern):
    """
    Compute the Longest Proper Prefix which is also Suffix (LPS) array.
    
    Args:
        pattern (str): The pattern string to compute LPS for.
    
    Returns:
        list: The LPS array for the given pattern.
    
    Raises:
        TypeError: If the input is not a string.
    """
    # Input validation
    if not isinstance(pattern, str):
        raise TypeError("Pattern must be a string")
    
    # Initialize LPS array with zeros
    lps = [0] * len(pattern)
    
    # Length of the previous longest prefix suffix
    length = 0
    
    # Index for the current position
    i = 1
    
    while i < len(pattern):
        # If characters match, extend the prefix
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            # If characters don't match
            if length != 0:
                # Go back to the previous matching prefix
                length = lps[length - 1]
            else:
                # No matching prefix found
                lps[i] = 0
                i += 1
    
    return lps

def kmp_search(text, pattern):
    """
    Perform KMP string matching to find all occurrences of a pattern in a text.
    
    Args:
        text (str): The text to search in.
        pattern (str): The pattern to search for.
    
    Returns:
        list: Indices of all occurrences of the pattern in the text.
    
    Raises:
        TypeError: If inputs are not strings.
        ValueError: If pattern is an empty string.
    """
    # Input validation
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise TypeError("Both text and pattern must be strings")
    
    if not pattern:
        raise ValueError("Pattern cannot be an empty string")
    
    # Compute the LPS array for the pattern
    lps = compute_lps_array(pattern)
    
    # Result list to store all matches
    matches = []
    
    # Pointers for text and pattern
    text_idx = 0
    pattern_idx = 0
    
    while text_idx < len(text):
        # If characters match, move both pointers
        if text[text_idx] == pattern[pattern_idx]:
            text_idx += 1
            pattern_idx += 1
        
        # If full pattern is matched, record the match
        if pattern_idx == len(pattern):
            matches.append(text_idx - pattern_idx)
            # Continue searching by updating pattern index to allow overlapping matches
            pattern_idx = lps[pattern_idx - 1]
        
        # If characters don't match and we're not at the start of pattern
        elif text_idx < len(text) and text[text_idx] != pattern[pattern_idx]:
            # If not at the start of pattern, use LPS array to skip comparisons
            if pattern_idx != 0:
                pattern_idx = lps[pattern_idx - 1]
            else:
                # Move to next character in text
                text_idx += 1
    
    return matches
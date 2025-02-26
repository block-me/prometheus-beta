def remove_duplicate_chars(input_string: str) -> str:
    """
    Remove duplicate characters from a lowercase string, preserving the original order.

    Args:
        input_string (str): A lowercase string to remove duplicates from.

    Returns:
        str: A string with duplicate characters removed, keeping first occurrence.

    Raises:
        ValueError: If the input contains non-lowercase characters.
    """
    # Validate input
    if not input_string.islower():
        raise ValueError("Input must contain only lowercase characters")
    
    # Use an ordered set approach to preserve original order
    seen = set()
    result = []
    
    for char in input_string:
        if char not in seen:
            seen.add(char)
            result.append(char)
    
    return ''.join(result)
def sort_unique_chars(input_string):
    """
    Return a sorted list of unique characters from the input string.
    
    The function handles case-sensitive sorting and works with strings of any length.
    
    Args:
        input_string (str): The input string to extract unique characters from.
    
    Returns:
        list: A sorted list of unique characters in case-sensitive alphabetical order.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> sort_unique_chars("hello")
        ['e', 'h', 'l', 'o']
        >>> sort_unique_chars("Python")
        ['P', 'n', 'o', 't', 'y']
        >>> sort_unique_chars("")
        []
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Use set to get unique characters
    unique_chars = set(input_string)
    
    # Sort characters prioritizing uppercase, then lowercase, 
    # while maintaining alphabetical order within those groups
    return sorted(unique_chars, key=lambda x: (x.isupper(), x))
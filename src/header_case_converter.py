def convert_to_header_case(text: str) -> str:
    """
    Convert a given string to header case.
    
    Header case capitalizes the first letter of each word, similar to title case,
    but with specific handling for different input formats.
    
    Args:
        text (str): The input string to convert to header case.
    
    Returns:
        str: The input string converted to header case.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> convert_to_header_case("hello world")
        'Hello World'
        >>> convert_to_header_case("hello_world")
        'Hello World'
        >>> convert_to_header_case("hello-world")
        'Hello World'
        >>> convert_to_header_case("helloWorld")
        'Hello World'
    """
    # Validate input
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Replace common separators with spaces
    normalized = text.replace('_', ' ').replace('-', ' ')
    
    # Handle camelCase by inserting spaces before capital letters
    chars = []
    for i, char in enumerate(normalized):
        if i > 0 and char.isupper() and normalized[i-1].islower():
            chars.append(' ')
        chars.append(char)
    
    # Convert to space-separated string and title case
    return ''.join(chars).title()
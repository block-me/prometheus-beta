def convert_to_alternating_case(input_string):
    """
    Convert a string to alternating sentence case.
    
    Args:
        input_string (str): The input string to be converted.
    
    Returns:
        str: The string converted to alternating sentence case.
    
    Raises:
        TypeError: If input is not a string.
    
    Examples:
        >>> convert_to_alternating_case("hello world")
        'Hello wOrLd'
        >>> convert_to_alternating_case("PYTHON IS AWESOME")
        'PyThOn Is AwEsOmE'
        >>> convert_to_alternating_case("")
        ''
    """
    # Check input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string 
    if not input_string:
        return ""
    
    # Convert to alternating case
    result = []
    for i, char in enumerate(input_string):
        if i % 2 == 0:
            result.append(char.upper())
        else:
            result.append(char.lower())
    
    return ''.join(result)
import logging

def log_multiline(message, level='info', separator='=', separator_length=40):
    """
    Log a multi-line message with optional separators.

    Args:
        message (str): The message to be logged
        level (str, optional): Logging level. Defaults to 'info'.
            Supports 'debug', 'info', 'warning', 'error', 'critical'
        separator (str, optional): Character used for separation lines. Defaults to '='.
        separator_length (int, optional): Length of separator lines. Defaults to 40.

    Raises:
        ValueError: If an invalid logging level is provided
        TypeError: If inputs are of incorrect type
    """
    # Validate inputs
    if not isinstance(message, str):
        raise TypeError("Message must be a string")
    
    if not isinstance(separator, str) or len(separator) != 1:
        raise ValueError("Separator must be a single character")
    
    if not isinstance(separator_length, int) or separator_length < 1:
        raise ValueError("Separator length must be a positive integer")

    # Normalize level to lowercase
    level = level.lower()

    # Select appropriate logging method
    log_methods = {
        'debug': logging.debug,
        'info': logging.info,
        'warning': logging.warning,
        'error': logging.error,
        'critical': logging.critical
    }

    if level not in log_methods:
        raise ValueError(f"Invalid logging level: {level}")

    # Create log method
    log_func = log_methods[level]

    # Create separator line
    sep_line = separator * separator_length

    # Log with separators
    log_func(sep_line)
    
    # Split and log each line of the message
    for line in message.split('\n'):
        log_func(line)
    
    log_func(sep_line)
"""
A simple module for logging messages to the console.

This module provides a straightforward function to log messages 
with optional log levels and formatting.
"""

def log_message(message, level='INFO'):
    """
    Log a message to the console with an optional log level.

    Args:
        message (str): The message to be logged.
        level (str, optional): The log level. Defaults to 'INFO'.
                                Supported levels: 'INFO', 'WARNING', 'ERROR', 'DEBUG'

    Raises:
        TypeError: If message is not a string.
        ValueError: If an invalid log level is provided.
    """
    # Validate input types
    if not isinstance(message, str):
        raise TypeError("Message must be a string")

    # Validate log level
    valid_levels = ['INFO', 'WARNING', 'ERROR', 'DEBUG']
    level = level.upper()
    if level not in valid_levels:
        raise ValueError(f"Invalid log level. Must be one of {valid_levels}")

    # Format and print the log message
    formatted_message = f"[{level}] {message}"
    print(formatted_message)
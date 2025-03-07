import sys
import logging
from typing import Optional, TextIO

def log_user_input(log_file: Optional[str] = None) -> str:
    """
    Capture and log user input from the command line.

    Args:
        log_file (Optional[str], optional): Path to the log file. 
                                            If None, logs to the default system log.

    Returns:
        str: The user input that was logged.

    Raises:
        ValueError: If the input is empty or contains only whitespace.
    """
    # Ensure a unique logger for each call
    logger = logging.getLogger(f'user_input_logger_{id(log_file)}')
    logger.handlers.clear()  # Remove any existing handlers
    
    # Configure logging
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
    else:
        # Use a StreamHandler for default logging
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
        logger.addHandler(stream_handler)
        logger.setLevel(logging.INFO)

    # Prompt and capture user input
    try:
        user_input = input("Enter your input: ").strip()
        
        # Validate input
        if not user_input:
            raise ValueError("Input cannot be empty")
        
        # Log the input
        logger.info(user_input)
        
        return user_input
    except (KeyboardInterrupt, EOFError):
        logger.info("Input operation cancelled")
        raise
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
    # Configure logging
    if log_file:
        logging.basicConfig(
            filename=log_file, 
            level=logging.INFO, 
            format='%(asctime)s - %(message)s'
        )
    else:
        logging.basicConfig(
            level=logging.INFO, 
            format='%(asctime)s - %(message)s'
        )

    # Prompt and capture user input
    try:
        user_input = input("Enter your input: ").strip()
        
        # Validate input
        if not user_input:
            raise ValueError("Input cannot be empty")
        
        # Log the input
        logging.info(user_input)
        
        return user_input
    except (KeyboardInterrupt, EOFError):
        logging.info("Input operation cancelled")
        raise
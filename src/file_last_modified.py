import os
from datetime import datetime

def get_file_last_modified(file_path):
    """
    Get the last modified date of a file.
    
    Args:
        file_path (str): Path to the file.
    
    Returns:
        datetime: The last modified timestamp of the file.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        TypeError: If the file_path is not a string.
    """
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string")
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    modified_timestamp = os.path.getmtime(file_path)
    return datetime.fromtimestamp(modified_timestamp)
import os
from typing import Optional, Union


def find_oldest_file(directory: Union[str, os.PathLike]) -> Optional[str]:
    """
    Find the oldest file in a given directory.

    Args:
        directory (str or os.PathLike): Path to the directory to search.

    Returns:
        Optional[str]: Path to the oldest file, or None if no files exist.

    Raises:
        FileNotFoundError: If the specified directory does not exist.
        NotADirectoryError: If the specified path is not a directory.
    """
    # Validate input directory
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory not found: {directory}")
    
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"Path is not a directory: {directory}")
    
    # Get all files in the directory
    files = [
        os.path.join(directory, f) 
        for f in os.listdir(directory) 
        if os.path.isfile(os.path.join(directory, f))
    ]
    
    # If no files exist, return None
    if not files:
        return None
    
    # Find the oldest file based on creation time
    return min(files, key=os.path.getctime)
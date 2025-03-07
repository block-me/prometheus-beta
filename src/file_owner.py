import os
import pwd

def get_file_owner(file_path):
    """
    Get the owner of a file by its path.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The username of the file owner.

    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If there's no permission to access file metadata.
    """
    # Validate input
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string")
    
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    try:
        # Get file stats and retrieve owner's username
        file_stat = os.stat(file_path)
        return pwd.getpwuid(file_stat.st_uid).pw_name
    except PermissionError:
        raise PermissionError(f"Cannot access metadata for file: {file_path}")
    except Exception as e:
        raise RuntimeError(f"Unexpected error retrieving file owner: {str(e)}")
import os
import shutil

def copy_file(source_path, destination_path):
    """
    Copy a file from source path to destination path.

    Args:
        source_path (str): Path to the source file to be copied.
        destination_path (str): Path where the file should be copied to.

    Raises:
        FileNotFoundError: If the source file does not exist.
        PermissionError: If there are insufficient permissions to copy the file.
        IsADirectoryError: If source_path is a directory instead of a file.
        ValueError: If source and destination paths are the same.
    """
    # Validate input paths
    if not isinstance(source_path, str) or not isinstance(destination_path, str):
        raise TypeError("Paths must be strings")

    # Normalize paths to handle different path formats
    source_path = os.path.abspath(source_path)
    destination_path = os.path.abspath(destination_path)

    # Check if source and destination are the same
    if source_path == destination_path:
        raise ValueError("Source and destination paths must be different")

    # Check if source file exists
    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Source file not found: {source_path}")

    # Check if source is a file (not a directory)
    if not os.path.isfile(source_path):
        raise IsADirectoryError(f"Source path is not a file: {source_path}")

    # Ensure destination directory exists
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)

    try:
        # Use shutil for robust file copying
        shutil.copy2(source_path, destination_path)
    except PermissionError:
        raise PermissionError(f"Permission denied when copying from {source_path} to {destination_path}")
import os

def read_file_line_by_line(file_path):
    """
    Read a file line by line and return its contents as a list of strings.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        list: A list of strings, where each string is a line from the file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        IsADirectoryError: If the path points to a directory instead of a file.
        IOError: If there is an error reading the file.
    """
    # Pre-check file status
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' was not found.")
    
    if os.path.isdir(file_path):
        raise IsADirectoryError(f"'{file_path}' is a directory, not a file.")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Using .readlines() with rstrip() to handle different newline scenarios
            return [line.rstrip('\r\n') for line in file.readlines()]
    except IOError as e:
        raise IOError(f"An error occurred while reading the file: {e}")
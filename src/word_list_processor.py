def process_word_list(file_path):
    """
    Read words from a text file, remove duplicates, and return a sorted unique list of words.

    Args:
        file_path (str): Path to the text file containing words.

    Returns:
        list: A sorted list of unique words from the file.

    Raises:
        FileNotFoundError: If the specified file cannot be found.
        IOError: If there's an error reading the file.
    """
    try:
        # Read the file and split into words
        with open(file_path, 'r') as file:
            # Read lines, strip whitespace, convert to lowercase to handle case-insensitive duplicates
            words = [word.strip().lower() for word in file.readlines()]
        
        # Remove duplicates and sort
        unique_words = sorted(set(words))
        
        return unique_words
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except IOError as e:
        raise IOError(f"An error occurred while reading the file: {e}")
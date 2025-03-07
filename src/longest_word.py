import string

def find_longest_word(sentence):
    """
    Find the longest word in a given sentence.

    Args:
        sentence (str): The input sentence to search for the longest word.

    Returns:
        str: The longest word in the sentence. 
             If multiple words have the same maximum length, returns the first one.
             Returns an empty string for empty input or sentences with no words.

    Raises:
        TypeError: If input is not a string.
    """
    # Check for invalid input
    if not isinstance(sentence, str):
        raise TypeError("Input must be a string")
    
    # Remove punctuation and split into words
    # Use string.punctuation to remove all punctuation marks
    translator = str.maketrans('', '', string.punctuation)
    words = sentence.translate(translator).strip().split()
    
    # Return empty string if no words
    if not words:
        return ""
    
    # Find the longest word (first occurrence in case of tie)
    return max(words, key=len)
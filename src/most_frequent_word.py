def most_frequent_word(text: str) -> str:
    """
    Find the most frequently occurring word in a given text.

    Args:
        text (str): A string of lowercase words separated by spaces.

    Returns:
        str: The most frequently occurring word in the text.
             If multiple words have the same highest frequency, 
             returns one of those words.

    Raises:
        ValueError: If the input text is empty or contains non-lowercase letters.

    Examples:
        >>> most_frequent_word("the quick brown fox jumps over the lazy dog")
        'the'
        >>> most_frequent_word("a b c a b a")
        'a'
    """
    # Validate input
    if not text:
        raise ValueError("Input text cannot be empty")
    
    # Check for non-lowercase letters
    if not text.islower():
        raise ValueError("Input text must contain only lowercase letters")
    
    # Split the text into words
    words = text.split()
    
    # If no words, raise an error
    if not words:
        raise ValueError("No words found in the input text")
    
    # Count word frequencies
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    
    # Find the most frequent word
    return max(word_counts, key=word_counts.get)
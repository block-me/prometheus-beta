def count_vowels_consonants(text):
    """
    Count the number of vowels and consonants in a given string.
    
    Args:
        text (str): The input string to analyze.
    
    Returns:
        dict: A dictionary with 'vowels' and 'consonants' counts.
    
    Raises:
        TypeError: If input is not a string.
    """
    # Check input type
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Convert to lowercase to simplify counting
    text = text.lower()
    
    # Define vowels
    vowels = set('aeiou')
    
    # Initialize counters
    vowel_count = 0
    consonant_count = 0
    
    # Count vowels and consonants
    for char in text:
        # Skip non-alphabetic characters
        if not char.isalpha():
            continue
        
        # Count vowels and consonants
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
    
    # Return results as a dictionary
    return {
        'vowels': vowel_count,
        'consonants': consonant_count
    }
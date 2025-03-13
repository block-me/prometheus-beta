def isAnagram(str1: str, str2: str) -> bool:
    """
    Check if two strings are anagrams of each other.

    An anagram is a word or phrase formed by rearranging the letters of another word or phrase,
    using all the original letters exactly once. The check is case-insensitive and 
    ignores whitespace and punctuation.

    Args:
        str1 (str): The first input string
        str2 (str): The second input string

    Returns:
        bool: True if the strings are anagrams, False otherwise

    Raises:
        TypeError: If either input is not a string
    """
    # Validate input types
    if not (isinstance(str1, str) and isinstance(str2, str)):
        raise TypeError("Both inputs must be strings")
    
    # Remove non-alphanumeric characters and convert to lowercase
    def clean_string(s: str) -> str:
        return ''.join(char.lower() for char in s if char.isalnum())
    
    # Compare character counts
    cleaned_str1 = clean_string(str1)
    cleaned_str2 = clean_string(str2)
    
    # Quick length check
    if len(cleaned_str1) != len(cleaned_str2):
        return False
    
    # Use character counting to verify anagram
    return sorted(cleaned_str1) == sorted(cleaned_str2)
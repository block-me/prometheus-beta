def multiply_even_numbers(numbers):
    """
    Takes an array of numbers and returns a new array with all even numbers multiplied by 2.
    
    Args:
        numbers (list): A list of integers to process
    
    Returns:
        list: A new list with even numbers doubled and odd numbers unchanged
    
    Raises:
        TypeError: If the input is not a list or contains non-numeric elements
    """
    # Validate input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Process the list, multiplying even numbers by 2
    return [num * 2 if num % 2 == 0 else num for num in numbers]
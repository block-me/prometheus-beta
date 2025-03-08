def generate_odd_fibonacci_sequence(n):
    """
    Generate a Fibonacci sequence containing only odd numbers.
    
    Args:
        n (int): The desired length of the sequence. Must be a non-negative integer.
    
    Returns:
        list: A list of n odd Fibonacci numbers.
    
    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Sequence length must be non-negative")
    
    # Special case handling for small sequence lengths
    if n == 0:
        return []
    
    if n == 1:
        return [1]
    
    # Initialize the sequence with the first two odd Fibonacci numbers
    sequence = [1, 1]
    
    # Generate the rest of the sequence
    while len(sequence) < n:
        # Calculate the next number in the sequence
        next_num = sequence[-1] + sequence[-2]
        
        # Ensure only odd numbers are added
        next_num = next_num if next_num % 2 != 0 else next_num + 1
        
        sequence.append(next_num)
    
    return sequence
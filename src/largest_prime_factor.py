def find_largest_prime_factor(n):
    """
    Find the largest prime factor of a given positive integer.

    Args:
        n (int): A positive integer greater than 1.

    Returns:
        int: The largest prime factor of the input number.

    Raises:
        ValueError: If the input is less than 2.
        TypeError: If the input is not an integer.
    """
    # Input validation
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 2:
        raise ValueError("Input must be a positive integer greater than 1")
    
    # Find largest prime factor using trial division
    largest_prime_factor = 1
    
    # First, handle even numbers by dividing out 2
    while n % 2 == 0:
        largest_prime_factor = 2
        n //= 2
    
    # Then check odd factors up to sqrt(n)
    factor = 3
    while factor * factor <= n:
        # If factor divides n, it's a prime factor
        while n % factor == 0:
            largest_prime_factor = factor
            n //= factor
        
        # Move to next potential prime factor
        factor += 2
    
    # If n is still > 1, it means n itself is prime
    if n > 1:
        largest_prime_factor = max(largest_prime_factor, n)
    
    return largest_prime_factor
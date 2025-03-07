def recursive_gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) of two integers using recursion.
    
    This function implements the Euclidean algorithm recursively to find 
    the greatest common divisor of two non-negative integers.
    
    Args:
        a (int): First non-negative integer
        b (int): Second non-negative integer
    
    Returns:
        int: The greatest common divisor of a and b
    
    Raises:
        ValueError: If either input is negative
        TypeError: If inputs are not integers
    """
    # Type checking
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Inputs must be integers")
    
    # Validate non-negative inputs
    if a < 0 or b < 0:
        raise ValueError("Inputs must be non-negative integers")
    
    # Base case: if b is 0, return a
    if b == 0:
        return a
    
    # Recursive case: gcd(a,b) = gcd(b, a % b)
    return recursive_gcd(b, a % b)
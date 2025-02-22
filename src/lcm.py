def calculate_lcm(a: int, b: int) -> int:
    """
    Calculate the Least Common Multiple (LCM) of two numbers.
    
    Args:
        a (int): First number
        b (int): Second number
    
    Returns:
        int: The least common multiple of a and b
    
    Raises:
        ValueError: If either input is less than or equal to 0
    """
    # Check for non-positive inputs
    if a <= 0 or b <= 0:
        raise ValueError("Input numbers must be positive integers")
    
    # Use the GCD method to calculate LCM
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    
    # LCM(a,b) = |a * b| / GCD(a,b)
    return abs(a * b) // gcd(a, b)
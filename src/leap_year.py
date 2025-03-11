def is_leap_year(year: int) -> bool:
    """
    Determine if a given year is a leap year.
    
    A leap year is defined by the following rules:
    - The year must be divisible by 4
    - If the year is divisible by 100, it must also be divisible by 400 to be a leap year
    
    Args:
        year (int): The year to check
    
    Returns:
        bool: True if the year is a leap year, False otherwise
    
    Raises:
        ValueError: If the input year is not a positive integer
    """
    # Validate input
    if not isinstance(year, int):
        raise ValueError("Year must be an integer")
    
    if year <= 0:
        raise ValueError("Year must be a positive integer")
    
    # Leap year criteria
    if year % 4 == 0:
        if year % 100 == 0:
            # Years divisible by 100 must also be divisible by 400 to be a leap year
            return year % 400 == 0
        return True
    
    return False
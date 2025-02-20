import random
import string

def generate_verification_code():
    """
    Generate a unique 6-digit verification code.
    
    Returns:
        str: A 6-digit verification code consisting of digits 0-9.
    """
    return ''.join(random.choices(string.digits, k=6))

def validate_verification_code(code):
    """
    Validate a verification code.
    
    Args:
        code (str): The verification code to validate.
    
    Returns:
        bool: True if the code is valid, False otherwise.
    """
    # Check if the code is a 6-digit string consisting only of digits
    return (
        isinstance(code, str) and 
        len(code) == 6 and 
        code.isdigit()
    )
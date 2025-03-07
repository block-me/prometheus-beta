import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

def log_variable_type(variable):
    """
    Log the type of a given variable.

    This function takes any variable as input and logs its type using the logging module.
    It handles different types of variables, including None.

    Args:
        variable: Any Python variable to determine and log its type.

    Returns:
        str: The string representation of the variable's type.
    """
    # Determine the type of the variable
    if variable is None:
        var_type = "NoneType"
    else:
        var_type = type(variable).__name__

    # Log the type
    logger.info(f"Variable type: {var_type}")
    
    return var_type
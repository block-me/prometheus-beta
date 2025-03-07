import logging

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
    # Set up basic logging configuration if not already configured
    logging.basicConfig(level=logging.INFO, format='%(message)s')

    # Handle None separately as type(None) returns NoneType
    if variable is None:
        logging.info("Variable type: NoneType")
        return "NoneType"

    # Get the type of the variable and log it
    var_type = type(variable).__name__
    logging.info(f"Variable type: {var_type}")
    return var_type
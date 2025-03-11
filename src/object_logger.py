import json
import logging
import pprint
import inspect

def log_object(obj, log_level=logging.INFO, logger_name='default_logger'):
    """
    Log an object in a readable, formatted manner.

    Args:
        obj (any): The object to be logged
        log_level (int, optional): Logging level. Defaults to logging.INFO.
        logger_name (str, optional): Name of the logger. Defaults to 'default_logger'.

    Returns:
        str: A formatted string representation of the object

    Raises:
        TypeError: If the object cannot be serialized
    """
    # Create or get the logger
    logger = logging.getLogger(logger_name)

    try:
        # Try JSON serialization first (for JSON-serializable objects)
        try:
            json_str = json.dumps(obj, indent=2)
            formatted_output = f"JSON Representation:\n{json_str}"
        except (TypeError, ValueError):
            # If JSON fails, check if the object has a dict or repr representation
            if hasattr(obj, '__dict__'):
                # Use object's __dict__ for custom objects
                obj_dict = obj.__dict__
                json_str = json.dumps(obj_dict, indent=2)
                formatted_output = f"Object Dictionary Representation:\n{json_str}"
            else:
                # Fallback to string representation
                str_repr = str(obj)
                formatted_output = f"String Representation:\n{str_repr}"

        # Log the formatted output at the specified log level
        log_method = getattr(logger, logging.getLevelName(log_level).lower())
        log_method(formatted_output)

        return formatted_output

    except Exception as e:
        # Handle any unexpected serialization errors
        error_msg = f"Could not log object: {str(e)}"
        logger.error(error_msg)
        raise TypeError(error_msg) from e
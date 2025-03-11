import json
import logging
import pprint

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
            # If JSON fails, use pretty print
            formatter = pprint.PrettyPrinter(indent=2)
            formatted_output = f"Pretty Print Representation:\n{formatter.pformat(obj)}"

        # Log the formatted output at the specified log level
        log_method = getattr(logger, logging.getLevelName(log_level).lower())
        log_method(formatted_output)

        return formatted_output

    except Exception as e:
        # Handle any unexpected serialization errors
        error_msg = f"Could not log object: {str(e)}"
        logger.error(error_msg)
        raise TypeError(error_msg) from e
from termcolor import colored

def log_colored_message(message, color='green'):
    """
    Log a message in a specified color to the console.

    Args:
        message (str): The message to log.
        color (str, optional): The color to use. Defaults to 'green'.
            Supported colors: 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'.

    Raises:
        ValueError: If an unsupported color is provided.
        TypeError: If the message is not a string or the color is not a string.
    """
    # Validate input types
    if not isinstance(message, str):
        raise TypeError("Message must be a string")
    
    if not isinstance(color, str):
        raise TypeError("Color must be a string")
    
    # Supported colors 
    supported_colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    
    # Validate color
    if color.lower() not in supported_colors:
        raise ValueError(f"Unsupported color. Supported colors are: {', '.join(supported_colors)}")
    
    # Print colored message
    print(colored(message, color.lower()))
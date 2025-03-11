import readline
import logging
from typing import Optional, Callable

class ReadlineLogger:
    """
    A utility class for logging interactive readline prompts.
    
    This class provides methods to log user inputs captured through readline,
    with configurable logging options and error handling.
    """
    
    def __init__(self, logger: Optional[logging.Logger] = None):
        """
        Initialize the ReadlineLogger.
        
        Args:
            logger (Optional[logging.Logger]): Custom logger. 
                If not provided, a default logger will be created.
        """
        self.logger = logger or logging.getLogger(__name__)
        self._original_hook = readline.get_completer()
    
    def start_logging(self, log_level: int = logging.INFO) -> None:
        """
        Start logging readline inputs.
        
        Args:
            log_level (int): Logging level for the captured inputs. 
                Defaults to logging.INFO.
        """
        def logging_hook(text: str) -> None:
            """
            Internal hook to log readline inputs.
            
            Args:
                text (str): The input text to be logged.
            """
            try:
                self.logger.log(log_level, f"Readline Input: {text}")
            except Exception as e:
                self.logger.error(f"Error logging readline input: {e}")
        
        # Set the new logging completer hook
        readline.set_completer(logging_hook)
    
    def stop_logging(self) -> None:
        """
        Stop logging readline inputs and restore the original completer hook.
        """
        # Restore the original completer hook
        readline.set_completer(self._original_hook)
    
    def log_input(self, prompt: str, log_level: int = logging.INFO) -> str:
        """
        Capture and log user input with a specific prompt.
        
        Args:
            prompt (str): The prompt to display to the user.
            log_level (int): Logging level for the captured input.
        
        Returns:
            str: The user's input.
        
        Raises:
            ValueError: If the input is empty or None.
        """
        try:
            user_input = input(prompt)
            
            if not user_input:
                raise ValueError("Input cannot be empty")
            
            self.logger.log(log_level, f"Logged Input - Prompt: {prompt}, Value: {user_input}")
            return user_input
        except Exception as e:
            self.logger.error(f"Error capturing input: {e}")
            raise
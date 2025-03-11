import pytest
import logging
import readline
import io
import sys
from unittest.mock import patch, MagicMock

from src.readline_logger import ReadlineLogger

class TestReadlineLogger:
    @pytest.fixture
    def mock_logger(self):
        """Create a mock logger for testing."""
        logger = logging.getLogger('test_logger')
        logger.setLevel(logging.INFO)
        return logger
    
    def test_initialization(self, mock_logger):
        """Test logger initialization with custom and default loggers."""
        logger1 = ReadlineLogger()
        assert logger1.logger is not None
        
        logger2 = ReadlineLogger(mock_logger)
        assert logger2.logger == mock_logger
    
    def test_start_and_stop_logging(self, mock_logger):
        """Test starting and stopping readline logging."""
        rl_logger = ReadlineLogger(mock_logger)
        
        # Store the original completer
        original_completer = readline.get_completer()
        
        # Start logging
        rl_logger.start_logging()
        assert readline.get_completer() is not None
        
        # Stop logging, should restore original completer
        rl_logger.stop_logging()
        assert readline.get_completer() == original_completer
    
    @patch('builtins.input', return_value='test input')
    def test_log_input_successful(self, mock_input, mock_logger, caplog):
        """Test successful input logging."""
        caplog.set_level(logging.INFO)
        
        rl_logger = ReadlineLogger(mock_logger)
        result = rl_logger.log_input("Test Prompt: ")
        
        assert result == 'test input'
        assert "Logged Input - Prompt: Test Prompt: " in caplog.text
        assert "Value: test input" in caplog.text
    
    @patch('builtins.input', return_value='')
    def test_log_input_empty_input(self, mock_input, mock_logger):
        """Test handling of empty input."""
        rl_logger = ReadlineLogger(mock_logger)
        
        with pytest.raises(ValueError, match="Input cannot be empty"):
            rl_logger.log_input("Test Prompt: ")
    
    def test_logging_hook_error_handling(self, mock_logger):
        """Test error handling in logging hook."""
        rl_logger = ReadlineLogger(mock_logger)
        
        # Simulate a logging error
        with patch.object(mock_logger, 'log', side_effect=Exception("Log error")):
            with patch.object(mock_logger, 'error') as mock_error:
                # Start logging and test the hook
                rl_logger.start_logging()
                
                # Simulate completer hook call
                completer = readline.get_completer()
                completer("test")
                
                # Verify error was logged
                mock_error.assert_called_once_with("Error logging readline input: Log error")
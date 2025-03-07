import os
import pytest
import logging
import tempfile
from unittest.mock import patch
from src.user_input_logger import log_user_input

def test_log_user_input_with_file():
    """Test logging user input to a file"""
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_log:
        temp_log_path = temp_log.name

    try:
        # Simulate user input
        with patch('builtins.input', return_value='Test input'):
            result = log_user_input(log_file=temp_log_path)
        
        # Check return value
        assert result == 'Test input'
        
        # Check log file contents
        with open(temp_log_path, 'r') as log_file:
            log_contents = log_file.read()
            assert 'Test input' in log_contents
    finally:
        # Clean up the temp file
        os.unlink(temp_log_path)

def test_log_user_input_empty_input():
    """Test that empty input raises a ValueError"""
    with patch('builtins.input', return_value='   '):
        with pytest.raises(ValueError, match="Input cannot be empty"):
            log_user_input()

def test_log_user_input_keyboard_interrupt():
    """Test handling of keyboard interrupt"""
    with patch('builtins.input', side_effect=KeyboardInterrupt):
        with pytest.raises(KeyboardInterrupt):
            log_user_input()

def test_log_user_input_eof():
    """Test handling of EOF condition"""
    with patch('builtins.input', side_effect=EOFError):
        with pytest.raises(EOFError):
            log_user_input()

def test_log_user_input_default_logging():
    """Test logging without specifying a log file"""
    # Capture log messages
    with patch('logging.Logger.info') as mock_log:
        with patch('builtins.input', return_value='Default log test'):
            result = log_user_input()
        
        # Check return value
        assert result == 'Default log test'
        
        # Verify logging was called
        mock_log.assert_called_once_with('Default log test')
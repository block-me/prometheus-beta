"""
Tests for the console logger module.
"""

import pytest
import sys
from io import StringIO
from src.console_logger import log_message

def test_default_log_level(capsys):
    """Test logging with default INFO level."""
    log_message("Test message")
    captured = capsys.readouterr()
    assert captured.out.strip() == "[INFO] Test message"

def test_different_log_levels(capsys):
    """Test logging with different log levels."""
    test_cases = [
        ('WARNING', "[WARNING] Warning message"),
        ('ERROR', "[ERROR] Error message"),
        ('DEBUG', "[DEBUG] Debug message")
    ]
    
    for level, expected_output in test_cases:
        log_message("Test message", level)
        captured = capsys.readouterr()
        assert captured.out.strip() == expected_output

def test_invalid_log_level():
    """Test that an invalid log level raises a ValueError."""
    with pytest.raises(ValueError, match="Invalid log level"):
        log_message("Test message", "INVALID")

def test_non_string_message():
    """Test that non-string messages raise a TypeError."""
    with pytest.raises(TypeError, match="Message must be a string"):
        log_message(123)
    
    with pytest.raises(TypeError, match="Message must be a string"):
        log_message(None)
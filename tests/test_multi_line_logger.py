import pytest
import logging
from io import StringIO
import sys

from src.multi_line_logger import log_multiline

@pytest.fixture
def captured_logs():
    """Fixture to capture log output"""
    log_capture = StringIO()
    handler = logging.StreamHandler(log_capture)
    logging.getLogger().addHandler(handler)
    logging.getLogger().setLevel(logging.DEBUG)
    
    yield log_capture
    
    logging.getLogger().removeHandler(handler)
    handler.close()

def test_basic_multiline_logging(captured_logs):
    """Test basic multi-line logging"""
    test_message = "First line\nSecond line\nThird line"
    log_multiline(test_message)
    
    log_output = captured_logs.getvalue()
    assert "First line" in log_output
    assert "Second line" in log_output
    assert "Third line" in log_output
    assert log_output.count('=' * 40) == 2  # Start and end separators

def test_different_log_levels(captured_logs):
    """Test logging at different levels"""
    levels = ['debug', 'info', 'warning', 'error', 'critical']
    
    for level in levels:
        captured_logs.truncate(0)
        captured_logs.seek(0)
        
        test_message = f"Test message at {level} level"
        log_multiline(test_message, level=level)
        
        log_output = captured_logs.getvalue()
        assert test_message in log_output

def test_custom_separator(captured_logs):
    """Test custom separator character and length"""
    test_message = "Custom separator test"
    log_multiline(test_message, separator='#', separator_length=20)
    
    log_output = captured_logs.getvalue()
    assert test_message in log_output
    assert log_output.count('#' * 20) == 2

def test_empty_message(captured_logs):
    """Test logging an empty message"""
    log_multiline("")
    
    log_output = captured_logs.getvalue()
    assert log_output.count('=' * 40) == 2

def test_input_validation():
    """Test input validation"""
    # Non-string message
    with pytest.raises(TypeError):
        log_multiline(123)
    
    # Invalid separator
    with pytest.raises(ValueError):
        log_multiline("Test", separator="too long")
    
    # Invalid separator length
    with pytest.raises(ValueError):
        log_multiline("Test", separator_length=0)
    
    # Invalid log level
    with pytest.raises(ValueError):
        log_multiline("Test", level="invalid")
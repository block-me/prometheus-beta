import pytest
from io import StringIO
import sys
from src.colored_logger import log_colored_message
from termcolor import colored

def test_default_green_color(capsys):
    """Test default green color logging."""
    log_colored_message("Test message")
    captured = capsys.readouterr()
    assert captured.out.strip() == colored("Test message", 'green')

def test_different_colors(capsys):
    """Test logging with different supported colors."""
    colors = ['red', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    for color in colors:
        log_colored_message("Test message", color)
        captured = capsys.readouterr()
        assert captured.out.strip() == colored("Test message", color)

def test_invalid_color():
    """Test that an unsupported color raises a ValueError."""
    with pytest.raises(ValueError, match="Unsupported color"):
        log_colored_message("Test message", "purple")

def test_non_string_message():
    """Test that a non-string message raises a TypeError."""
    with pytest.raises(TypeError, match="Message must be a string"):
        log_colored_message(123)

def test_non_string_color():
    """Test that a non-string color raises a TypeError."""
    with pytest.raises(TypeError, match="Color must be a string"):
        log_colored_message("Test message", 123)

def test_case_insensitive_color(capsys):
    """Test that color matching is case-insensitive."""
    log_colored_message("Test message", "GREEN")
    captured = capsys.readouterr()
    assert captured.out.strip() == colored("Test message", 'green')
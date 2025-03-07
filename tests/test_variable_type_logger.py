import pytest
import logging
import io
import sys
from src.variable_type_logger import log_variable_type

def test_log_variable_type_int():
    """Test logging type for an integer."""
    # Capture log output
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.INFO)

    # Call the function
    result = log_variable_type(42)

    # Check the type and log message
    assert result == "int"
    assert "Variable type: int" in log_capture.getvalue().strip()

def test_log_variable_type_str():
    """Test logging type for a string."""
    # Capture log output
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.INFO)

    # Call the function
    result = log_variable_type("hello")

    # Check the type and log message
    assert result == "str"
    assert "Variable type: str" in log_capture.getvalue().strip()

def test_log_variable_type_list():
    """Test logging type for a list."""
    # Capture log output
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.INFO)

    # Call the function
    result = log_variable_type([1, 2, 3])

    # Check the type and log message
    assert result == "list"
    assert "Variable type: list" in log_capture.getvalue().strip()

def test_log_variable_type_none():
    """Test logging type for None."""
    # Capture log output
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.INFO)

    # Call the function
    result = log_variable_type(None)

    # Check the type and log message
    assert result == "NoneType"
    assert "Variable type: NoneType" in log_capture.getvalue().strip()

def test_log_variable_type_custom_class():
    """Test logging type for a custom class."""
    class TestClass:
        pass

    test_instance = TestClass()

    # Capture log output
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.INFO)

    # Call the function
    result = log_variable_type(test_instance)

    # Check the type and log message
    assert result == "TestClass"
    assert "Variable type: TestClass" in log_capture.getvalue().strip()
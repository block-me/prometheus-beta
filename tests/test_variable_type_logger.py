import pytest
import logging
import io
import sys
from src.variable_type_logger import log_variable_type

def test_log_variable_type_int():
    """Test logging type for an integer."""
    # Capture log output
    log_capture = io.StringIO()
    log_handler = logging.StreamHandler(log_capture)
    logger = logging.getLogger(__name__)
    logger.addHandler(log_handler)
    logger.setLevel(logging.INFO)

    # Call the function
    result = log_variable_type(42)

    # Check the type and log message
    log_output = log_capture.getvalue().strip()
    assert result == "int"
    assert "Variable type: int" in log_output

def test_log_variable_type_str():
    """Test logging type for a string."""
    # Capture log output
    log_capture = io.StringIO()
    log_handler = logging.StreamHandler(log_capture)
    logger = logging.getLogger(__name__)
    logger.addHandler(log_handler)
    logger.setLevel(logging.INFO)

    # Call the function
    result = log_variable_type("hello")

    # Check the type and log message
    log_output = log_capture.getvalue().strip()
    assert result == "str"
    assert "Variable type: str" in log_output

def test_log_variable_type_list():
    """Test logging type for a list."""
    # Capture log output
    log_capture = io.StringIO()
    log_handler = logging.StreamHandler(log_capture)
    logger = logging.getLogger(__name__)
    logger.addHandler(log_handler)
    logger.setLevel(logging.INFO)

    # Call the function
    result = log_variable_type([1, 2, 3])

    # Check the type and log message
    log_output = log_capture.getvalue().strip()
    assert result == "list"
    assert "Variable type: list" in log_output

def test_log_variable_type_none():
    """Test logging type for None."""
    # Capture log output
    log_capture = io.StringIO()
    log_handler = logging.StreamHandler(log_capture)
    logger = logging.getLogger(__name__)
    logger.addHandler(log_handler)
    logger.setLevel(logging.INFO)

    # Call the function
    result = log_variable_type(None)

    # Check the type and log message
    log_output = log_capture.getvalue().strip()
    assert result == "NoneType"
    assert "Variable type: NoneType" in log_output

def test_log_variable_type_custom_class():
    """Test logging type for a custom class."""
    class TestClass:
        pass

    test_instance = TestClass()

    # Capture log output
    log_capture = io.StringIO()
    log_handler = logging.StreamHandler(log_capture)
    logger = logging.getLogger(__name__)
    logger.addHandler(log_handler)
    logger.setLevel(logging.INFO)

    # Call the function
    result = log_variable_type(test_instance)

    # Check the type and log message
    log_output = log_capture.getvalue().strip()
    assert result == "TestClass"
    assert "Variable type: TestClass" in log_output
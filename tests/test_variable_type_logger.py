import pytest
import sys
import io
from src.variable_type_logger import log_variable_type

def test_log_variable_type_int(capsys):
    """Test logging type for an integer."""
    # Call the function
    result = log_variable_type(42)

    # Capture output and check the type and output
    captured = capsys.readouterr()
    assert result == "int"
    assert "Variable type: int" in captured.out.strip()

def test_log_variable_type_str(capsys):
    """Test logging type for a string."""
    # Call the function
    result = log_variable_type("hello")

    # Capture output and check the type and output
    captured = capsys.readouterr()
    assert result == "str"
    assert "Variable type: str" in captured.out.strip()

def test_log_variable_type_list(capsys):
    """Test logging type for a list."""
    # Call the function
    result = log_variable_type([1, 2, 3])

    # Capture output and check the type and output
    captured = capsys.readouterr()
    assert result == "list"
    assert "Variable type: list" in captured.out.strip()

def test_log_variable_type_none(capsys):
    """Test logging type for None."""
    # Call the function
    result = log_variable_type(None)

    # Capture output and check the type and output
    captured = capsys.readouterr()
    assert result == "NoneType"
    assert "Variable type: NoneType" in captured.out.strip()

def test_log_variable_type_custom_class(capsys):
    """Test logging type for a custom class."""
    class TestClass:
        pass

    test_instance = TestClass()

    # Call the function
    result = log_variable_type(test_instance)

    # Capture output and check the type and output
    captured = capsys.readouterr()
    assert result == "TestClass"
    assert "Variable type: TestClass" in captured.out.strip()
import os
import pytest
from datetime import datetime, timedelta
import sys

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.file_last_modified import get_file_last_modified

def test_get_file_last_modified(tmp_path):
    # Create a test file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Test content")
    
    # Get the last modified date
    modified_date = get_file_last_modified(str(test_file))
    
    # Check that the modified date is recent (within last few seconds)
    assert isinstance(modified_date, datetime)
    assert datetime.now() - modified_date < timedelta(seconds=5)

def test_get_file_last_modified_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        get_file_last_modified("nonexistent_file.txt")

def test_get_file_last_modified_invalid_input():
    with pytest.raises(TypeError):
        get_file_last_modified(123)  # Non-string input
    with pytest.raises(TypeError):
        get_file_last_modified(None)  # None input
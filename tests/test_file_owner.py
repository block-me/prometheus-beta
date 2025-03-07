import os
import pytest
import getpass
from src.file_owner import get_file_owner

def test_get_file_owner_current_user():
    """Test that function returns current user for an existing file."""
    # Create a temporary file owned by current user
    temp_file_path = "tests/temp_file.txt"
    with open(temp_file_path, 'w') as f:
        f.write("Test content")
    
    try:
        current_user = getpass.getuser()
        owner = get_file_owner(temp_file_path)
        assert owner == current_user
    finally:
        # Clean up the temporary file
        os.remove(temp_file_path)

def test_get_file_owner_invalid_input():
    """Test handling of invalid input types."""
    with pytest.raises(TypeError):
        get_file_owner(123)
    with pytest.raises(TypeError):
        get_file_owner(None)

def test_get_file_owner_nonexistent_file():
    """Test handling of non-existent file."""
    with pytest.raises(FileNotFoundError):
        get_file_owner("non_existent_file.txt")

def test_get_file_owner_input_validation():
    """Test input validation for file path."""
    with pytest.raises(TypeError):
        get_file_owner(["invalid", "path"])
    with pytest.raises(TypeError):
        get_file_owner({"not": "a path"})
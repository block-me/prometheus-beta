import os
import pytest
import shutil
from src.file_copy import copy_file

@pytest.fixture
def temp_source_file(tmp_path):
    """Create a temporary source file for testing."""
    source_file = tmp_path / "source_file.txt"
    source_file.write_text("Test content")
    return str(source_file)

def test_successful_file_copy(temp_source_file, tmp_path):
    """Test successful file copying."""
    dest_file = str(tmp_path / "destination_file.txt")
    copy_file(temp_source_file, dest_file)
    assert os.path.exists(dest_file)
    assert open(temp_source_file, 'r').read() == open(dest_file, 'r').read()

def test_copy_to_existing_directory(temp_source_file, tmp_path):
    """Test copying to an existing directory."""
    dest_dir = tmp_path / "subdir"
    dest_dir.mkdir()
    dest_file = str(dest_dir / "destination_file.txt")
    copy_file(temp_source_file, dest_file)
    assert os.path.exists(dest_file)

def test_source_file_not_found(tmp_path):
    """Test copying a non-existent source file."""
    with pytest.raises(FileNotFoundError):
        copy_file(str(tmp_path / "nonexistent.txt"), str(tmp_path / "dest.txt"))

def test_source_and_destination_same(temp_source_file):
    """Test copying to the same file path."""
    with pytest.raises(ValueError):
        copy_file(temp_source_file, temp_source_file)

def test_source_is_directory(tmp_path):
    """Test attempting to copy a directory."""
    with pytest.raises(IsADirectoryError):
        copy_file(str(tmp_path), str(tmp_path / "destination.txt"))

def test_invalid_path_types():
    """Test passing non-string path types."""
    with pytest.raises(TypeError):
        copy_file(123, "dest.txt")
    with pytest.raises(TypeError):
        copy_file("source.txt", None)
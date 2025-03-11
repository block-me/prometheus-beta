import os
import tempfile
import pytest
from datetime import datetime, timedelta
from src.oldest_file import find_oldest_file


def test_find_oldest_file_with_multiple_files():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create multiple files with different creation times
        file1_path = os.path.join(temp_dir, 'file1.txt')
        file2_path = os.path.join(temp_dir, 'file2.txt')
        file3_path = os.path.join(temp_dir, 'file3.txt')

        # Create first file and set its creation time to oldest
        with open(file1_path, 'w') as f:
            f.write('file1')
        os.utime(file1_path, (datetime.now().timestamp() - 100, datetime.now().timestamp() - 100))

        # Create second file with a more recent creation time
        with open(file2_path, 'w') as f:
            f.write('file2')
        os.utime(file2_path, (datetime.now().timestamp() - 50, datetime.now().timestamp() - 50))

        # Create third file with the most recent creation time
        with open(file3_path, 'w') as f:
            f.write('file3')

        # Find the oldest file
        oldest_file = find_oldest_file(temp_dir)
        
        # Assert that the oldest file is correctly identified
        assert oldest_file == file1_path


def test_find_oldest_file_with_empty_directory():
    # Create a temporary empty directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Find the oldest file
        oldest_file = find_oldest_file(temp_dir)
        
        # Assert that None is returned
        assert oldest_file is None


def test_find_oldest_file_raises_file_not_found():
    # Test that FileNotFoundError is raised for non-existent directory
    with pytest.raises(FileNotFoundError):
        find_oldest_file('/path/to/non/existent/directory')


def test_find_oldest_file_raises_not_a_directory():
    # Create a temporary file
    with tempfile.NamedTemporaryFile() as temp_file:
        # Test that NotADirectoryError is raised when a file path is provided
        with pytest.raises(NotADirectoryError):
            find_oldest_file(temp_file.name)


def test_find_oldest_file_with_single_file():
    # Create a temporary directory with a single file
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, 'single_file.txt')
        
        # Create the file
        with open(file_path, 'w') as f:
            f.write('content')
        
        # Find the oldest file
        oldest_file = find_oldest_file(temp_dir)
        
        # Assert the file is correctly identified
        assert oldest_file == file_path
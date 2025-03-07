import os
import pytest
from src.file_reader import read_file_line_by_line

def test_read_file_line_by_line_normal():
    # Create a temporary test file
    test_file_path = 'tests/test_file.txt'
    with open(test_file_path, 'w', encoding='utf-8') as f:
        f.write("First line\nSecond line\nThird line")
    
    try:
        # Test reading the file
        result = read_file_line_by_line(test_file_path)
        assert result == ["First line", "Second line", "Third line"]
    finally:
        # Clean up the test file
        os.remove(test_file_path)

def test_read_file_line_by_line_empty_file():
    # Create an empty test file
    test_file_path = 'tests/empty_test_file.txt'
    with open(test_file_path, 'w', encoding='utf-8') as f:
        pass
    
    try:
        # Test reading an empty file
        result = read_file_line_by_line(test_file_path)
        assert result == []
    finally:
        # Clean up the test file
        os.remove(test_file_path)

def test_read_file_line_by_line_file_not_found():
    # Test file not found scenario
    with pytest.raises(FileNotFoundError):
        read_file_line_by_line('non_existent_file.txt')

def test_read_file_line_by_line_with_newline_characters():
    # Create a test file with various newline characters
    test_file_path = 'tests/newline_test_file.txt'
    with open(test_file_path, 'w', encoding='utf-8') as f:
        f.write("Line 1\n\nLine 2\n\n\nLine 3")
    
    try:
        # Test reading file with multiple newline characters
        result = read_file_line_by_line(test_file_path)
        assert result == ["Line 1", "", "Line 2", "", "", "Line 3"]
    finally:
        # Clean up the test file
        os.remove(test_file_path)
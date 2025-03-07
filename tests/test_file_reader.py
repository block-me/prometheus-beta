import os
import tempfile
import pytest
from src.file_reader import read_file_line_by_line

def test_read_file_line_by_line_normal():
    with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as temp_file:
        temp_file.write("First line\nSecond line\nThird line")
        temp_file.close()
    
    try:
        result = read_file_line_by_line(temp_file.name)
        assert result == ["First line", "Second line", "Third line"]
    finally:
        os.unlink(temp_file.name)

def test_read_file_line_by_line_empty_file():
    with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as temp_file:
        temp_file.close()
    
    try:
        result = read_file_line_by_line(temp_file.name)
        assert result == []
    finally:
        os.unlink(temp_file.name)

def test_read_file_line_by_line_file_not_found():
    with pytest.raises(FileNotFoundError):
        read_file_line_by_line('non_existent_file.txt')

def test_read_file_line_by_line_with_newline_characters():
    with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as temp_file:
        temp_file.write("Line 1\n\nLine 2\n\n\nLine 3")
        temp_file.close()
    
    try:
        result = read_file_line_by_line(temp_file.name)
        assert result == ["Line 1", "", "Line 2", "", "", "Line 3"]
    finally:
        os.unlink(temp_file.name)

def test_read_file_line_by_line_directory_error():
    with pytest.raises(IsADirectoryError):
        read_file_line_by_line('.')  # Current directory

def test_read_file_line_by_line_permission_error(tmp_path):
    # Create a file and make it unreadable
    # We'll use a different approach to test permission handling
    unreadable_file = tmp_path / 'unreadable_file.txt'
    unreadable_file.write_text('Test content')
    
    # Change file ownership to a different user
    try:
        import pwd
        import os
        nobody_uid = pwd.getpwnam('nobody').pw_uid
        os.chown(str(unreadable_file), nobody_uid, -1)
    except (ImportError, KeyError):
        # Fallback to permission manipulation if user changing isn't possible
        unreadable_file.chmod(0o000)
    
    try:
        with pytest.raises((PermissionError, OSError)):
            read_file_line_by_line(str(unreadable_file))
    finally:
        # Restore permissions to allow cleanup
        unreadable_file.chmod(0o644)
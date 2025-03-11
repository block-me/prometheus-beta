import os
import pytest
import zipfile
import tempfile
from src.zip_extractor import extract_zip_files
import shutil


@pytest.fixture
def sample_zip_file():
    """Create a sample zip file for testing."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a zip file with multiple files
        zip_path = os.path.join(temp_dir, 'test_archive.zip')
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            zipf.writestr('file1.txt', 'Content of file 1')
            zipf.writestr('file2.txt', 'Content of file 2')
            zipf.writestr('subfolder/file3.txt', 'Content of file 3')
        
        yield zip_path


def test_extract_zip_files_default_path(sample_zip_file):
    """Test extracting zip files to default path."""
    extracted_files = extract_zip_files(sample_zip_file)
    
    # Check number of extracted files
    assert len(extracted_files) == 3
    
    # Verify files exist
    for file_path in extracted_files:
        assert os.path.exists(file_path)
    
    # Clean up extracted files
    extracted_dir = os.path.dirname(extracted_files[0])
    shutil.rmtree(extracted_dir)


def test_extract_zip_files_custom_path(sample_zip_file):
    """Test extracting zip files to a custom path."""
    with tempfile.TemporaryDirectory() as custom_dir:
        extracted_files = extract_zip_files(sample_zip_file, custom_dir)
        
        # Check number of extracted files
        assert len(extracted_files) == 3
        
        # Verify files exist in custom path
        for file_path in extracted_files:
            assert os.path.exists(file_path)
            assert file_path.startswith(custom_dir)


def test_extract_nonexistent_zip():
    """Test extracting from a non-existent zip file."""
    with pytest.raises(FileNotFoundError):
        extract_zip_files('nonexistent_file.zip')


def test_extract_invalid_zip_file():
    """Test extracting from an invalid zip file."""
    with tempfile.NamedTemporaryFile(suffix='.zip', delete=False) as temp_file:
        temp_file.write(b'This is not a valid zip file')
        temp_file_path = temp_file.name
    
    try:
        with pytest.raises(ValueError):
            extract_zip_files(temp_file_path)
    finally:
        os.unlink(temp_file_path)


def test_extract_wrong_extension():
    """Test extracting from a file without .zip extension."""
    with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as temp_file:
        temp_file.write(b'This is a text file')
        temp_file_path = temp_file.name
    
    try:
        with pytest.raises(ValueError):
            extract_zip_files(temp_file_path)
    finally:
        os.unlink(temp_file_path)
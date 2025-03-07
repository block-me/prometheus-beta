import os
import pytest
import tarfile
import tempfile
import shutil

from src.tar_extractor import extract_tar_archive

@pytest.fixture
def temp_dir():
    """Create a temporary directory for testing."""
    temp_path = tempfile.mkdtemp()
    yield temp_path
    # Cleanup after test
    shutil.rmtree(temp_path)

@pytest.fixture
def sample_tar_archive(temp_dir):
    """Create a sample tar archive for testing."""
    archive_path = os.path.join(temp_dir, 'sample.tar')
    
    # Create a tar archive with some test files
    with tarfile.open(archive_path, 'w') as tar:
        # Create some test files
        test_files = [
            ('file1.txt', b'Content of file 1'),
            ('file2.txt', b'Content of file 2'),
            ('subdir/file3.txt', b'Content of file 3')
        ]
        
        for filename, content in test_files:
            file_path = os.path.join(temp_dir, filename)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            
            with open(file_path, 'wb') as f:
                f.write(content)
            
            tar.add(file_path, arcname=filename)
    
    return archive_path

def test_extract_full_archive(sample_tar_archive, temp_dir):
    """Test extracting all files from a tar archive."""
    extracted_files = extract_tar_archive(sample_tar_archive, temp_dir)
    
    assert len(extracted_files) == 3
    assert all(os.path.exists(f) for f in extracted_files)
    assert set(os.path.basename(f) for f in extracted_files) == {'file1.txt', 'file2.txt', 'file3.txt'}

def test_extract_specific_files(sample_tar_archive, temp_dir):
    """Test extracting specific files from a tar archive."""
    extracted_files = extract_tar_archive(sample_tar_archive, temp_dir, ['file1.txt'])
    
    assert len(extracted_files) == 1
    assert os.path.basename(extracted_files[0]) == 'file1.txt'

def test_extract_to_default_path(sample_tar_archive, temp_dir):
    """Test extracting to the default path (archive directory)."""
    os.chdir(temp_dir)  # Change current working directory
    extracted_files = extract_tar_archive(sample_tar_archive)
    
    assert len(extracted_files) == 3
    assert all(os.path.exists(f) for f in extracted_files)

def test_nonexistent_archive():
    """Test extracting from a nonexistent archive raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        extract_tar_archive('/path/to/nonexistent/archive.tar')

def test_invalid_tar_archive(temp_dir):
    """Test extracting an invalid tar archive raises ValueError."""
    invalid_archive = os.path.join(temp_dir, 'invalid.tar')
    
    # Create an invalid archive file
    with open(invalid_archive, 'wb') as f:
        f.write(b'Invalid tar content')
    
    with pytest.raises(ValueError):
        extract_tar_archive(invalid_archive)

def test_empty_specific_files(sample_tar_archive, temp_dir):
    """Test extracting with an empty list of specific files."""
    extracted_files = extract_tar_archive(sample_tar_archive, temp_dir, [])
    
    assert len(extracted_files) == 0
import pytest
import bz2
from src.bzip2_compression import compress_bzip2, decompress_bzip2

def test_compress_string():
    """Test compressing a string"""
    original = "Hello, world! This is a test of Bzip2 compression."
    compressed = compress_bzip2(original)
    assert isinstance(compressed, bytes)
    assert len(compressed) < len(original.encode('utf-8'))

def test_compress_bytes():
    """Test compressing bytes"""
    original = b"Binary data for compression test"
    compressed = compress_bzip2(original)
    assert isinstance(compressed, bytes)
    assert len(compressed) < len(original)

def test_decompress():
    """Test full compression and decompression cycle"""
    original = "Hello, world! This is a test of Bzip2 compression."
    compressed = compress_bzip2(original)
    decompressed = decompress_bzip2(compressed)
    assert decompressed.decode('utf-8') == original

def test_different_compression_levels():
    """Test different compression levels"""
    data = "Test data for compression level verification"
    # Test various compression levels
    for level in range(1, 10):
        compressed = compress_bzip2(data, compression_level=level)
        assert isinstance(compressed, bytes)

def test_invalid_compression_level():
    """Test invalid compression levels"""
    with pytest.raises(ValueError):
        compress_bzip2("test", compression_level=0)
    with pytest.raises(ValueError):
        compress_bzip2("test", compression_level=10)

def test_invalid_input_type():
    """Test invalid input types"""
    with pytest.raises(TypeError):
        compress_bzip2(123)
    with pytest.raises(TypeError):
        decompress_bzip2("not bytes")

def test_empty_input():
    """Test compressing and decompressing empty input"""
    empty_string = ""
    empty_bytes = b""
    
    # String compression
    compressed_str = compress_bzip2(empty_string)
    decompressed_str = decompress_bzip2(compressed_str)
    assert decompressed_str.decode('utf-8') == empty_string

    # Bytes compression
    compressed_bytes = compress_bzip2(empty_bytes)
    decompressed_bytes = decompress_bzip2(compressed_bytes)
    assert decompressed_bytes == empty_bytes

def test_large_input():
    """Test compressing a large input"""
    large_data = "A" * 100000  # 100,000 character string
    compressed = compress_bzip2(large_data)
    decompressed = decompress_bzip2(compressed)
    assert decompressed.decode('utf-8') == large_data
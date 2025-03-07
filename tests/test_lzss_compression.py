"""
Test suite for LZSS Compression Algorithm.

This module contains comprehensive tests for the LZSSCompressor class,
covering various scenarios and edge cases.
"""

import pytest
import random
import string

from src.lzss_compression import LZSSCompressor


def generate_random_string(length):
    """Generate a random string of specified length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def test_lzss_compressor_initialization():
    """Test initializing LZSSCompressor with default and custom parameters."""
    compressor = LZSSCompressor()
    assert compressor.window_size == 4096
    assert compressor.lookahead_size == 16

    custom_compressor = LZSSCompressor(window_size=2048, lookahead_size=8)
    assert custom_compressor.window_size == 2048
    assert custom_compressor.lookahead_size == 8


def test_empty_input():
    """Test compression and decompression of empty input."""
    compressor = LZSSCompressor()
    
    # Empty string
    empty_str = ''
    compressed = compressor.compress(empty_str)
    assert len(compressed) == 0
    
    decompressed = compressor.decompress(compressed)
    assert len(decompressed) == 0
    
    # Empty bytes
    empty_bytes = b''
    compressed = compressor.compress(empty_bytes)
    assert len(compressed) == 0
    
    decompressed = compressor.decompress(compressed)
    assert len(decompressed) == 0


def test_simple_compression_decompression():
    """Test basic compression and decompression scenarios."""
    compressor = LZSSCompressor()
    
    # Simple repeated string
    test_str = "hello hello world world"
    compressed = compressor.compress(test_str)
    
    # Verify compression is reasonable
    assert len(compressed) <= len(test_str.encode('utf-8')) * 1.5, \
        f"Compression size {len(compressed)} exceeds 1.5x original size {len(test_str.encode('utf-8'))}"
    
    # Decompress and verify
    decompressed = compressor.decompress(compressed)
    assert decompressed.decode('utf-8') == test_str


def test_complex_compression_scenarios():
    """Test compression with various input types and patterns."""
    compressor = LZSSCompressor()
    
    # Test cases: repeated patterns, mixed content
    test_cases = [
        "abcabcabcabc",  # Fully repeating pattern
        "The quick brown fox jumps over the lazy dog",  # Normal text
        "1234567812345678",  # Numeric repeats
        generate_random_string(1000),  # Large random string
    ]
    
    for test_str in test_cases:
        compressed = compressor.compress(test_str)
        decompressed = compressor.decompress(compressed)
        
        # Convert bytes to string for comparison if needed
        if isinstance(test_str, str):
            assert decompressed.decode('utf-8') == test_str
        else:
            assert decompressed == test_str


def test_byte_input():
    """Test compression with byte inputs."""
    compressor = LZSSCompressor()
    
    # Byte sequences with repetition
    test_bytes = b'\x01\x02\x03\x01\x02\x03\x04\x05\x06'
    compressed = compressor.compress(test_bytes)
    
    # Decompress and verify
    decompressed = compressor.decompress(compressed)
    assert decompressed == test_bytes


def test_error_handling():
    """Test error handling and edge cases."""
    compressor = LZSSCompressor()
    
    # Partial/truncated compressed data
    with pytest.raises(ValueError, match="Truncated compressed data"):
        compressor.decompress(b'\x00')  # Incomplete data
    
    with pytest.raises(ValueError, match="Incomplete match encoding"):
        compressor.decompress(b'\x00\x01')  # Incomplete match encoding
    
    with pytest.raises(ValueError, match="Invalid offset"):
        # Create an invalid decompression scenario with impossible offset
        compressor.decompress(b'\x00\xff\xff')


def test_compression_ratio():
    """Test that compression reduces data size for repetitive content."""
    compressor = LZSSCompressor()
    
    # Highly repetitive content
    repetitive_str = "ABCDEFG" * 1000
    original_size = len(repetitive_str.encode('utf-8'))
    
    compressed = compressor.compress(repetitive_str)
    decompressed = compressor.decompress(compressed)
    
    # Ensure some level of compression, but don't set too strict a threshold
    assert len(compressed) < original_size * 0.8, \
        f"Compression ratio not effective. Compressed: {len(compressed)}, Original: {original_size}"
    assert decompressed.decode('utf-8') == repetitive_str
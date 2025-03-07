"""
LZSS (Lempel-Ziv-Storer-Szymanski) Compression Algorithm Implementation.

This module provides functions for LZSS compression and decompression.
LZSS is a dictionary-based lossless compression algorithm that replaces 
repeated occurrences of data with references to a single copy.
"""

from typing import List, Union, Tuple


class LZSSCompressor:
    """
    LZSS Compression and Decompression Class.
    
    Implements the LZSS compression algorithm with configurable 
    sliding window and look-ahead buffer sizes.
    """
    
    def __init__(self, window_size: int = 4096, lookahead_size: int = 16):
        """
        Initialize the LZSS Compressor.
        
        Args:
            window_size (int): Size of the sliding window for searching previous matches. 
                                Default is 4096.
            lookahead_size (int): Size of the look-ahead buffer for finding matches. 
                                   Default is 16.
        """
        self.window_size = window_size
        self.lookahead_size = lookahead_size

    def compress(self, data: Union[str, bytes]) -> bytes:
        """
        Compress input data using LZSS algorithm.
        
        Args:
            data (str or bytes): Input data to compress
        
        Returns:
            bytes: Compressed data
        """
        # Convert input to bytes if it's a string
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        # Validate input
        if not data:
            return b''
        
        compressed = bytearray()
        current_pos = 0
        
        while current_pos < len(data):
            # Find the longest match in the sliding window
            best_length = 0
            best_offset = 0
            
            # Search window starts from the beginning of current window
            window_start = max(0, current_pos - self.window_size)
            
            # Look for longest match in sliding window
            for offset in range(1, current_pos - window_start + 1):
                match_length = 0
                
                # Check how long the match continues
                while (match_length < self.lookahead_size and 
                       current_pos + match_length < len(data) and
                       data[current_pos - offset + match_length] == 
                       data[current_pos + match_length]):
                    match_length += 1
                
                # Update best match if current match is longer
                if match_length > best_length:
                    best_length = match_length
                    best_offset = offset
            
            # Decide whether to use match or literal
            if best_length > 2:  # Matches longer than 2 are worth encoding
                # Encode match (offset, length)
                flags = 0  # Use 0 to indicate match
                compressed.append(flags)
                
                # Encode offset and length
                compressed.append(best_offset & 0xFF)
                compressed.append(
                    ((best_offset >> 8) & 0x0F) | 
                    ((best_length - 3) << 4)
                )
                current_pos += best_length
            else:
                # Encode literal
                flags = 1  # Use 1 to indicate literal
                compressed.append(flags)
                compressed.append(data[current_pos])
                current_pos += 1
        
        return bytes(compressed)

    def decompress(self, compressed: bytes) -> bytes:
        """
        Decompress LZSS compressed data.
        
        Args:
            compressed (bytes): Compressed input data
        
        Returns:
            bytes: Decompressed data
        
        Raises:
            ValueError: If the compressed data is truncated or invalid
        """
        # Validate input
        if not compressed:
            return b''
        
        decompressed = bytearray()
        i = 0
        
        while i < len(compressed):
            # Check if there's enough data to read
            if i + 1 >= len(compressed):
                raise ValueError("Truncated compressed data")
            
            # Check flag
            if compressed[i] == 0:  # Match
                if i + 2 >= len(compressed):
                    raise ValueError("Incomplete match encoding")
                
                # Extract offset and length
                offset = compressed[i+1] | ((compressed[i+2] & 0x0F) << 8)
                length = ((compressed[i+2] >> 4) & 0x0F) + 3
                
                # Validate offset
                if offset > len(decompressed):
                    raise ValueError(f"Invalid offset: {offset}")
                
                # Reconstruct match from previous data
                start = len(decompressed) - offset
                for j in range(length):
                    decompressed.append(decompressed[start + j])
                
                i += 3
            else:  # Literal
                # Add literal byte
                decompressed.append(compressed[i+1])
                i += 2
        
        return bytes(decompressed)
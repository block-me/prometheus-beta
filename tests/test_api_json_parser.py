"""
Unit tests for the API JSON parser function.

This test suite covers various scenarios including 
successful parsing, error handling, and edge cases.
"""

import pytest
import json
from src.api_json_parser import parse_api_response


def test_parse_valid_json_string():
    """Test parsing a valid JSON string."""
    json_str = '{"name": "John", "age": 30}'
    result = parse_api_response(json_str)
    assert result == {"name": "John", "age": 30}


def test_parse_valid_json_bytes():
    """Test parsing a valid JSON in bytes format."""
    json_bytes = b'{"name": "Jane", "city": "New York"}'
    result = parse_api_response(json_bytes)
    assert result == {"name": "Jane", "city": "New York"}


def test_parse_already_parsed_dict():
    """Test that a dictionary passes through unchanged."""
    input_dict = {"status": "success", "data": [1, 2, 3]}
    result = parse_api_response(input_dict)
    assert result == input_dict


def test_parse_empty_string():
    """Test that an empty string raises a ValueError."""
    with pytest.raises(ValueError, match="Response cannot be an empty string"):
        parse_api_response("")


def test_parse_none_input():
    """Test that None input raises a ValueError."""
    with pytest.raises(ValueError, match="Response cannot be None"):
        parse_api_response(None)


def test_parse_invalid_type():
    """Test that invalid input types raise a TypeError."""
    with pytest.raises(TypeError, match="Expected str, bytes, or dict"):
        parse_api_response(123)


def test_parse_malformed_json():
    """Test that malformed JSON raises a ValueError."""
    malformed_json = '{"name": "John", "age": }'
    with pytest.raises(ValueError, match="Invalid JSON format"):
        parse_api_response(malformed_json)


def test_parse_non_dict_json():
    """Test that non-dictionary JSON raises a TypeError."""
    list_json = json.dumps([1, 2, 3])
    with pytest.raises(TypeError, match="Parsed JSON must be a dictionary"):
        parse_api_response(list_json)


def test_parse_whitespace_json():
    """Test parsing JSON with surrounding whitespace."""
    whitespace_json = '  {"key": "value"}  '
    result = parse_api_response(whitespace_json)
    assert result == {"key": "value"}
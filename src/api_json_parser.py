"""
Module for parsing JSON responses from an API.

This module provides a utility function to parse JSON responses 
with robust error handling and type checking.
"""

import json
from typing import Any, Dict, Optional, Union


def parse_api_response(response: Union[str, bytes, Dict[str, Any]]) -> Dict[str, Any]:
    """
    Parse a JSON response from an API with comprehensive error handling.

    Args:
        response (Union[str, bytes, Dict[str, Any]]): The API response to parse.
            Can be a JSON string, bytes, or already parsed dictionary.

    Returns:
        Dict[str, Any]: A dictionary containing the parsed JSON data.

    Raises:
        ValueError: If the input is None, empty, or cannot be parsed.
        TypeError: If the input is not a string, bytes, or dictionary.
        json.JSONDecodeError: If the JSON is malformed.
    """
    # Check for None or empty input
    if response is None:
        raise ValueError("Response cannot be None")

    # If already a dictionary, return as-is
    if isinstance(response, dict):
        return response

    # Convert to string if bytes
    if isinstance(response, bytes):
        response = response.decode('utf-8')

    # Validate input type
    if not isinstance(response, str):
        raise TypeError(f"Expected str, bytes, or dict. Got {type(response).__name__}")

    # Strip whitespace
    response = response.strip()

    # Check for empty string
    if not response:
        raise ValueError("Response cannot be an empty string")

    try:
        # Parse JSON with strict parsing
        parsed_response = json.loads(response)

        # Ensure the parsed result is a dictionary
        if not isinstance(parsed_response, dict):
            raise TypeError(f"Parsed JSON must be a dictionary. Got {type(parsed_response).__name__}")

        return parsed_response

    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format: {str(e)}")
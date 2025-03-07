import pytest
from src.alternating_case import convert_to_alternating_case

def test_basic_string_conversion():
    """Test basic string conversion"""
    assert convert_to_alternating_case("hello world") == "HeLlO WoRlD"

def test_uppercase_string_conversion():
    """Test conversion of an uppercase string"""
    assert convert_to_alternating_case("PYTHON IS AWESOME") == "PyThOn Is AwEsOmE"

def test_mixed_case_string_conversion():
    """Test conversion of a mixed case string"""
    assert convert_to_alternating_case("MiXeD CaSe StRiNg") == "MiXeD CaSe StRiNg"

def test_empty_string():
    """Test conversion of an empty string"""
    assert convert_to_alternating_case("") == ""

def test_single_character():
    """Test conversion of a single character"""
    assert convert_to_alternating_case("a") == "A"
    assert convert_to_alternating_case("Z") == "Z"

def test_special_characters():
    """Test conversion of string with special characters"""
    assert convert_to_alternating_case("hello, world!") == "HeLlO, WoRlD!"

def test_invalid_input_type():
    """Test that TypeError is raised for non-string input"""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_alternating_case(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_alternating_case(None)

def test_whitespace_handling():
    """Test handling of whitespace characters"""
    assert convert_to_alternating_case("  spaces  ") == "  SpAcEs  "
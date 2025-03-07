import pytest
from src.header_case_converter import convert_to_header_case

def test_basic_space_separated():
    assert convert_to_header_case("hello world") == "Hello World"

def test_snake_case():
    assert convert_to_header_case("hello_world") == "Hello World"

def test_kebab_case():
    assert convert_to_header_case("hello-world") == "Hello World"

def test_camel_case():
    assert convert_to_header_case("helloWorld") == "Hello World"

def test_mixed_case():
    assert convert_to_header_case("hello_world-test") == "Hello World Test"

def test_single_word():
    assert convert_to_header_case("hello") == "Hello"

def test_empty_string():
    assert convert_to_header_case("") == ""

def test_already_header_case():
    assert convert_to_header_case("Hello World") == "Hello World"

def test_invalid_input_type():
    with pytest.raises(TypeError):
        convert_to_header_case(123)

def test_complex_camel_case():
    assert convert_to_header_case("helloWorldTest") == "Hello World Test"

def test_multiple_consecutive_separators():
    assert convert_to_header_case("hello__world") == "Hello World"
    assert convert_to_header_case("hello--world") == "Hello World"
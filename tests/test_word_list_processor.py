import os
import pytest
from src.word_list_processor import process_word_list

def test_process_word_list_normal_case(tmp_path):
    # Create a temporary file with test words
    test_file = tmp_path / "test_words.txt"
    test_file.write_text("apple\nbanana\ncherry\napple\nBANANA\ndate")
    
    # Process the file
    result = process_word_list(str(test_file))
    
    # Check expected output
    expected = ['apple', 'banana', 'cherry', 'date']
    assert result == expected, f"Expected {expected}, but got {result}"

def test_process_word_list_empty_file(tmp_path):
    # Create an empty temporary file
    test_file = tmp_path / "empty_words.txt"
    test_file.write_text("")
    
    # Process the file
    result = process_word_list(str(test_file))
    
    # Check for empty list
    assert result == [], "Expected an empty list for an empty file"

def test_process_word_list_file_not_found():
    # Test file not found scenario
    with pytest.raises(FileNotFoundError):
        process_word_list("non_existent_file.txt")

def test_process_word_list_whitespace_handling(tmp_path):
    # Create a file with words including whitespace
    test_file = tmp_path / "whitespace_words.txt"
    test_file.write_text("  apple  \n banana \n  cherry\n apple")
    
    # Process the file
    result = process_word_list(str(test_file))
    
    # Check expected output
    expected = ['apple', 'banana', 'cherry']
    assert result == expected, f"Expected {expected}, but got {result}"
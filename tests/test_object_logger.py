import logging
import pytest
import json
from src.object_logger import log_object

class CustomObject:
    def __init__(self, name, value):
        self.name = name
        self.value = value

def test_log_object_dict(caplog):
    """Test logging a dictionary"""
    test_dict = {"key1": "value1", "key2": 42}
    caplog.set_level(logging.INFO)
    
    result = log_object(test_dict)
    
    assert "JSON Representation" in result
    assert "key1" in result
    assert "value1" in result
    assert len(caplog.records) == 1
    assert caplog.records[0].levelno == logging.INFO

def test_log_object_list(caplog):
    """Test logging a list"""
    test_list = [1, 2, 3, "four"]
    caplog.set_level(logging.INFO)
    
    result = log_object(test_list)
    
    assert "JSON Representation" in result
    assert "1" in result
    assert "four" in result
    assert len(caplog.records) == 1
    assert caplog.records[0].levelno == logging.INFO

def test_log_object_custom_class(caplog):
    """Test logging a custom class object"""
    test_obj = CustomObject("Test", 123)
    caplog.set_level(logging.INFO)
    
    result = log_object(test_obj)
    
    assert "Object Dictionary Representation" in result
    assert "Test" in result
    assert "123" in result
    assert len(caplog.records) == 1
    assert caplog.records[0].levelno == logging.INFO

def test_log_object_different_log_level(caplog):
    """Test logging with a different log level"""
    test_dict = {"key": "value"}
    caplog.set_level(logging.DEBUG)
    
    result = log_object(test_dict, log_level=logging.DEBUG)
    
    assert "JSON Representation" in result
    assert len(caplog.records) == 1
    assert caplog.records[0].levelno == logging.DEBUG

def test_log_object_custom_logger(caplog):
    """Test logging with a custom logger name"""
    test_dict = {"key": "value"}
    caplog.set_level(logging.INFO)
    
    result = log_object(test_dict, logger_name="custom_logger")
    
    assert "JSON Representation" in result
    assert len(caplog.records) == 1
    assert caplog.records[0].levelname == "INFO"
    assert caplog.records[0].name == "custom_logger"

def test_log_object_primitive_types(caplog):
    """Test logging primitive types"""
    test_cases = [42, 3.14, "string", True, None]
    
    for value in test_cases:
        caplog.clear()
        result = log_object(value)
        
        assert "String Representation" in result
        assert str(value) in result
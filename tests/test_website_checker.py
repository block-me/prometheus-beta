import pytest
import requests
from src.website_checker import is_website_online

def test_valid_online_website():
    """Test that a known online website returns True."""
    assert is_website_online('https://www.google.com') == True

def test_nonexistent_website():
    """Test that a clearly invalid website returns False."""
    assert is_website_online('https://www.extremelyunlikelydomain123456.com') == False

def test_invalid_url_raises_error():
    """Test that empty or invalid URLs raise a ValueError."""
    with pytest.raises(ValueError):
        is_website_online('')
    
    with pytest.raises(ValueError):
        is_website_online(None)

def test_url_without_protocol():
    """Test that URLs without protocol are handled correctly."""
    assert is_website_online('google.com') == True

def test_custom_timeout():
    """Test custom timeout functionality."""
    # Test a very short timeout to simulate slow connection
    assert is_website_online('https://www.google.com', timeout=0.001) == False

def test_http_website():
    """Test an HTTP website to ensure protocol handling works."""
    assert is_website_online('http://httpbin.org') == True
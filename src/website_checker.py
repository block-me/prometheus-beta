import requests

def is_website_online(url: str, timeout: float = 5.0) -> bool:
    """
    Check if a website is online by attempting to establish a connection.
    
    Args:
        url (str): The full URL of the website to check (including http:// or https://)
        timeout (float, optional): Maximum time to wait for a response. Defaults to 5.0 seconds.
    
    Returns:
        bool: True if the website is online and accessible, False otherwise.
    
    Raises:
        ValueError: If the URL is invalid or empty.
    """
    # Validate input
    if not url or not isinstance(url, str):
        raise ValueError("URL must be a non-empty string")
    
    # Ensure URL starts with http:// or https://
    if not url.startswith(('http://', 'https://')):
        url = f'https://{url}'
    
    try:
        # Send a HEAD request to minimize data transfer
        response = requests.head(url, timeout=timeout)
        
        # Check if the response was successful (status code 200-299)
        return 200 <= response.status_code < 300
    
    except (requests.ConnectionError, requests.Timeout, requests.RequestException):
        # Connection failed or other request-related errors
        return False
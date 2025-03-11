import os
import zipfile
from typing import List, Union


def extract_zip_files(zip_path: str, extract_path: Union[str, None] = None) -> List[str]:
    """
    Extract all files from a zip archive to a specified destination.

    Args:
        zip_path (str): Path to the zip file to be extracted.
        extract_path (str, optional): Destination directory for extracted files. 
                                      If None, extracts to the zip file's directory.

    Returns:
        List[str]: List of paths to the extracted files.

    Raises:
        FileNotFoundError: If the zip file does not exist.
        ValueError: If the provided path is not a zip file.
        PermissionError: If there are insufficient permissions to extract files.
    """
    # Validate zip file existence
    if not os.path.exists(zip_path):
        raise FileNotFoundError(f"Zip file not found: {zip_path}")

    # Validate zip file extension
    if not zip_path.lower().endswith('.zip'):
        raise ValueError(f"File is not a zip archive: {zip_path}")

    # Determine extraction path
    if extract_path is None:
        extract_path = os.path.dirname(zip_path)
    
    # Ensure extraction directory exists
    os.makedirs(extract_path, exist_ok=True)

    # List to store extracted file paths
    extracted_files = []

    try:
        # Open and extract zip file
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # Extract all files
            for file in zip_ref.namelist():
                # Construct full file path
                full_path = zip_ref.extract(file, path=extract_path)
                extracted_files.append(full_path)

    except zipfile.BadZipFile:
        raise ValueError(f"Invalid or corrupted zip file: {zip_path}")
    except PermissionError:
        raise PermissionError(f"Permission denied when extracting files to {extract_path}")

    return extracted_files
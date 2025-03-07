import os
import tarfile
from typing import Union, List, Optional

def extract_tar_archive(archive_path: str, 
                         extract_path: Optional[str] = None, 
                         specific_files: Optional[List[str]] = None) -> List[str]:
    """
    Extract files from a tar archive.

    Args:
        archive_path (str): Path to the tar archive file.
        extract_path (Optional[str], optional): Directory to extract files to. 
            Defaults to the archive's directory if not specified.
        specific_files (Optional[List[str]], optional): List of specific files to extract. 
            Defaults to extracting all files. If an empty list, no files are extracted.

    Returns:
        List[str]: List of paths to extracted files.

    Raises:
        FileNotFoundError: If the archive file does not exist.
        ValueError: If the archive is invalid or cannot be opened.
        PermissionError: If there are insufficient permissions to extract.
    """
    # Validate archive path
    if not os.path.exists(archive_path):
        raise FileNotFoundError(f"Archive file not found: {archive_path}")

    # Determine extract path
    if extract_path is None:
        extract_path = os.path.dirname(os.path.abspath(archive_path))
    
    # Ensure extract path exists
    os.makedirs(extract_path, exist_ok=True)

    # List to store extracted file paths
    extracted_files = []

    # If specific_files is an empty list, return empty list immediately
    if specific_files is not None and len(specific_files) == 0:
        return extracted_files

    try:
        # Open the tar archive
        with tarfile.open(archive_path, 'r:*') as tar:
            # If specific files are provided, filter them
            if specific_files:
                members = [m for m in tar.getmembers() if m.name in specific_files]
            else:
                members = tar.getmembers()

            # Extract each member
            for member in members:
                # Prevent directory traversal attacks
                safe_path = os.path.normpath(os.path.join(extract_path, member.name))
                if not safe_path.startswith(os.path.abspath(extract_path)):
                    raise ValueError(f"Unsafe file path detected: {member.name}")

                # Extract the file
                tar.extract(member, path=extract_path)
                
                # Add to extracted files list
                extracted_files.append(os.path.join(extract_path, member.name))

    except tarfile.TarError as e:
        raise ValueError(f"Error extracting tar archive: {e}")
    except PermissionError:
        raise PermissionError(f"Insufficient permissions to extract archive: {archive_path}")

    return extracted_files
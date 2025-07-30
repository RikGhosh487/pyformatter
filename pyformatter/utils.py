import re


def should_format_file(file_path: str, include: str, exclude: str) -> bool:
    """Determine if the file should be formatted.

    This function checks if the file matches the include pattern
    and does not match the exclude pattern.

    Args:
        file_path (str): The path to the file.
        include (str): Regex pattern for files to include.
        exclude (str): Regex pattern for files to exclude.

    Returns:
        bool: True if the file should be formatted, False otherwise.
    """
    # Check if the file matches the include pattern
    if not re.search(include, file_path):
        return False

    # Check if the file matches the exclude pattern
    if exclude and re.search(exclude, file_path):
        return False

    return True

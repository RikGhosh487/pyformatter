import re


def should_format_file(
    file_path: str, compiled_include: re.Pattern, compiled_exclude: re.Pattern
) -> bool:
    """Determine if the file should be formatted.

    This function checks if the file matches the include pattern
    and does not match the exclude pattern.

    Args:
        file_path (str): The path to the file.
        compiled_include (re.Pattern): Compiled regex pattern for files to include.
        compiled_exclude (re.Pattern): Compiled regex pattern for files to exclude.

    Returns:
        bool: True if the file should be formatted, False otherwise.
    """
    # Check if the file matches the include pattern
    if not compiled_include.search(file_path):
        return False

    # Check if the file matches the exclude pattern
    if compiled_exclude and compiled_exclude.search(file_path):
        return False

    return True

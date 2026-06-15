"""
Recursive Directory Scanning

This module provides functionality to recursively scan a directory and its subdirectories,
collecting all Python files found.

"""
import os as os

#iterative solution
def scan_directory_iterative(directory):
    """
    Scans a directory and its subdirectories for Python files.

    Args:
        directory (str): The path to the directory to scan.

    Returns:
        list: A list of all .py files found.
        int: The number of .py files found.
    """
    python_files = []
    for root, dirs, files in os.walk(directory):
        print(root, dirs, files)
        for file in files:
            print(file)
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files, len(python_files)

#returned 398 .py files due to .venv
#Potential future improvements: exclude .venv and other virtual environment directories unless otherwise specified
print(scan_directory_iterative("."))

def scan_directory_recursive(directory):
    """
    Recursively scans a directory and its subdirectories for Python files.

    Args:
        directory (str): The path to the directory to scan.

    Returns:
        list: A list of all .py files found.
        int: The number of .py files found.
    """
    python_files = []
    for root, dirs, files in os.walk(directory):
        # Exclude virtual environment directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files, len(python_files)

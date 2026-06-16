"""
Recursive Directory Scanning

This module provides functionality to recursively scan a directory and its subdirectories,
collecting all Python files found.


reference: https://docs.python.org/3/library/pathlib.html

"""
import os as os
from pathlib import Path
#from rp import track_recursion
#from rp import measure_time


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
#print(scan_directory_iterative(".")

p = Path('.')
test_list =[x for x in p.iterdir() if x.is_dir()]
print(test_list)

#this will include all .py files in the current directory and all subdirectories
#print(list(p.glob("**/*.py")))

#can use pathlib classes for the recursive scanning

def scan_directory_recursive(path):
    """
    Recursively scans a directory and its subdirectories for Python files.

    Args:
        path (str | a path provided by the user): The path to the directory to scan

    Returns:
        list: A list of all .py files found.
        int: The number of .py files found.

    Think of this as a tree traversal problem, where each directory is a node and each subdirectory is a child node.

    
      A - starting point of any directory
     / \
    B   C - subdirectories of A
   / \
  D   E - subdirectories of B
    """

    #request path from user, turn it into pathlib object
    path = input("Enter the path to the directory to scan: ")
    path = Path(path)   
    print(f"Scanning {path}...")


    return 0

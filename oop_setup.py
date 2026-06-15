"""
Object-Oriented setup

Purpose: Create classes for the analyzer's core functionality and components.

For Milestone 1:
    - Could use a class to represent a directory
        - then can sort through the directory
            - some sort of function to recursively explore subdirectories
                - throughout the exploration, .py files will be collected, stored, then checked

        - directories have files
        - directories have subdirectories
        - directories need a filepath to be found

For Milestone 1:

- as of right now this is entirely unnecessary. I am going to solve this problem in main.py, continually test out base and edge cases to better understand the problem and find a solution.


"""

class Directory:
    def __init__(self, filepath):
        self.filepath = filepath
        self.files = []
        self.subdirectories = [[]]

    def add_file(self, file):
        self.files.append(file)

    def add_subdirectory(self, subdirectory):
        self.subdirectories.append(subdirectory)

current_directory = Directory("C:\system_graph")

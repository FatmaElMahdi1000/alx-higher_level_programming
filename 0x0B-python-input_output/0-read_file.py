#!/usr/bin/python3
"""reading text function from a file"""


def read_file(filename=""):
    """reads the name of the file"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")

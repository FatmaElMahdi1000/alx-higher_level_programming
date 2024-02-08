#!/usr/bin/python3

"""appending text function"""


def append_write(filename="", text=""):
    """appending"""
    with open(filename, "a", encoding='utf-8'):
        return f.write(text)

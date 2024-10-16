#!/usr/bin/python3
"""
validation

"""


def is_same_class(obj, a_class):
    """return True if the object is instance
    otherwise
    False"""
    return type(obj) is a_class

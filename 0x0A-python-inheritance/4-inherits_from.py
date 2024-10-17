#!usr/bin/python3
"""
checking if ab object a subclass
"""


def inherits_from(obj, a_class):
    return obj issubclass(a_class) and type(obj) is not a_class

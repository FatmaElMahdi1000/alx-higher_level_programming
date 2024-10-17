#!/usr/bin/python3
"""
checking if ab object a subclass
"""


def inherits_from(obj, a_class):
    """

    Returns True if the object is an instance of a class


    Args:
    obj: the obj to check
    a_class: the class to check against


    Returns:
           True, otherwise false
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class

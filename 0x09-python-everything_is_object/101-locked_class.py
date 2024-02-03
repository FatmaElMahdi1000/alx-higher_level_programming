#!/usr/bin/python3
# 101-locked_class.py
"""Defines a locked class."""


class LockedClass:
    """
    Preventing from instantiating new attributes
    but,'first_name'.
    """

    __slots__ = ["first_name"]

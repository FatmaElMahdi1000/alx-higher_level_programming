#!/usr/bin/python3
"""class-to-JSON function."""


def class_to_json(obj):
    """Return the dictionary represntation"""
    return obj.__dict__

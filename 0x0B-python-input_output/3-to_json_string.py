#!/usr/bin/python3
"""string-to-JSON function."""
import json


def to_json_string(my_obj):
    """function to convert data into JSON str"""
    return json.dumps(my_obj)

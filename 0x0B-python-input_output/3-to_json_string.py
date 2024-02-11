#!/usr/bin/python3
"""string-to-JSON function."""
import json


"""function to convert data into JSON str"""
def to_json_string(my_obj):
    return json.dumps(my_obj)

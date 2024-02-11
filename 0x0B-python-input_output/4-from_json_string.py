#!/usr/bin/python3
"""JSON object function"""


import json
def from_json_string(my_str):
    """decoding to the python"""
    return json.loads(my_str)

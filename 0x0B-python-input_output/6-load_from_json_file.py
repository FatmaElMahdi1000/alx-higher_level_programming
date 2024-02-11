#!/usr/bin/python3
"""creating an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """writing a function that creates an obj"""
    with open(filename) as f:
        text = json.load(f)
        return text

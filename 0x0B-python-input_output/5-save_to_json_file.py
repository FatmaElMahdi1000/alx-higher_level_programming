#!/usr/bin/python3

"""Object to a text file, using JSONrep."""
import json


def save_to_json_file(my_obj, filename):
    """JSON representation."""
    with open(filename, "w", encoding="utf-8") as f:
        text = f.writing(my_obj)
        updatedtext = json.dumps(text)
        return updatedtext

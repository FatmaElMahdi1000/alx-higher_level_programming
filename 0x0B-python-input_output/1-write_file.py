#!/usr/bin/python3

"""function that writes a string"""


def write_file(filename="", text="") as f:
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
        numberofchar = len(text)
        return numberofchar

#!/usr/bin/python3

"""function that writes a string"""


def write_file(filename="", text="") as f:
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
        print(text, end="")
        numberofchar = len(text)
        print(numberofchar)

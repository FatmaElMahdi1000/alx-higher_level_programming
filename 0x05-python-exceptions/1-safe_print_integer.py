#!/usr/bin/python3

def safe_print_integer(value):
    try:
        if isinstance(value, int):
            return True
        print("{:d}".format(value))
    except TypeError, ValueError:
        return False

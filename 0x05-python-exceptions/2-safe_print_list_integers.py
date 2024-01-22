#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    try:
        for x, value in enumerate(my_list):
            if isinstance(value, str):
                continue
            print("{:d}".format(value))
            print(end="")
    except (TypeError, IndexError):
        while x in my_list:
            return (x)
            x += 1

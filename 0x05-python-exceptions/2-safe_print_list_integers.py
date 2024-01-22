#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    M = 0
    try:
        for i, value in enumerate(range(0, x):
            if isinstance(value, str):
            print("{:d}".format(value))
            print(end="")
            M += 1
    except (TypeError, IndexError):
    continue
    print("")
    return (M)

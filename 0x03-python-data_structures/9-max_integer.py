#!/usr/bin/python3
def max_integer(my_list=[]):
    New_list = my_list.copy()
    New_list.sort()
    if my_list == "":
        None
    else:
        return New_list[-1]

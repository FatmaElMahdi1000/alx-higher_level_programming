#!/usr/bin/python3
def max_integer(my_list=[]):
    New_list = my_list.copy()
    New_list.sort()
    if len(my_list) > 0:
        return New_list[-1]
    else:
        None

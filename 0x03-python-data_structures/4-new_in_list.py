#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    if idx < 0 or idx >= my_list:
        return my_list
    New_list = my_list.copy()
    New_list[idx] = "element"
    return New_list

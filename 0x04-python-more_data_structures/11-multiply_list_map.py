#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    New_list = my_list.copy()
    multiplication = list(map(lambda x : x ** number, New_list))
    return multiplication

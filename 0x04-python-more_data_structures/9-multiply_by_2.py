#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    updated = {}
    for m in a_dictionary:
        updated[m] = a_dictionary[m] * 2
    return updated

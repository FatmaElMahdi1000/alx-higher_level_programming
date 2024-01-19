#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    updated_dictionary = map(lambda value: int(value)**2, a_dictionary.values())
    updated_dictionary = set(updated_dictionary)
    return updated_dictionary

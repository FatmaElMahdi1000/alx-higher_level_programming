#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):

    if key not in a_dictionary:
        a_dictionary[key] = [value]
    else:
        for N in a_dictionary:
            if N == key:
                a_dictionary[N] = value
    return a_dictionary

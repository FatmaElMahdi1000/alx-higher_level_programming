#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    updated = map(lambda kv: (kv[0], int(kv[1]**2), a_dictionary.items())
    updated = dict(updated)
    for key, value in updated.items():
       print("{:s}: {}".format(key, value))

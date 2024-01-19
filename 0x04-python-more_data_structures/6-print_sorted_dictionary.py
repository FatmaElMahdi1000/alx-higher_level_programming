#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for N in sorted(a_dictionary):
        print("{:s}: {}".format(N, a_dictionary[N]))

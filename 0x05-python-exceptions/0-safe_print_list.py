#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    N = 0
    try:
        while N is not x:
            print(imy_list[N], end=' ')
            N += 1
    except IndexError:
        None
        print()
        return N

#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    length1 = len(tuple_a)
    length2 = len(tuple_b)

    if length1 < 2:
        tuple_a.append(0)
    elif length2 < 2:
        tuple_b.append(0)
    else:
        t=((tuple_a[0]) + (tuple_b[0])), ((tuple_a[1]) + (tuple_b[1]))
        return t

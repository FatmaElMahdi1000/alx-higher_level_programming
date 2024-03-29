#!/usr/bin/python3

"""This is printing a square, Method"""


def print_square(size):
    """
    Args:
        size
    Output:
          square
    Raise:
         TypeError
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size is float and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        row = "#" * size
        print(row)

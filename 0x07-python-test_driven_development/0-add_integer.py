#!/usr/bin/python3
"""This is the "0-add_integer" method"""


def add_integer(a, b=98):
    """addition of intgers
    Args:
        a: first intger
        b: 98
    Raises:
    TypeError
    Returns:
           the sum
    """

    if not isinstance(a, int) and not isinstance(b, int):
        raise TypeError("must be an integer")
    elif isinstance(a, float) or isinstance(b, float):
        return int(a) + int(b)
    elif isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, int) and isinstance(b, float):
        return a + int(b)
    elif isinstance(a, float) and isinstance(b, int):
        return int(a) + b
    else:
        raise TypeError("must be an integer")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")

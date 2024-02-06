#!/usr/bin/python3

"""This is the "matrix" method"""


def matrix_divided(matrix, div):
    """Divide all elements of the matrix
    Args:
    matrix
    divisor

    local args:
    lists of lists
    ints
    """

    if not isinstance(div, int):
        raise TypeError("div must be a number")

    mylist = []

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if not isinstance(matrix, list):
        raise TypeError(
                "matrix must be a matrix (list of lists)")
    for Row in matrix:
        if not isinstance(Row, list):
            raise TypeError(
                    'matrix must be a matrix (list of lists) of integers/floats')
        if len(R) != len(R[:]):
            raise TypeError(
                    "Each row of the matrix must have the same size")
        for i, value in enumerate(R):
            if not isinstance(value, (int, float)):
                raise TypeError(
                        'matrix must be a matrix (list of lists) of integers/floats')

        return[[round(value/div, 2)]]

    if__name__ == "__main__":
        import doctest
        doctest.testfile("tests/2-matrix_divided.txt")

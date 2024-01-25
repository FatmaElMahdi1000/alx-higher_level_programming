#!/usr/bin/python3
"""square"""


class Square:
    """defining a square"""

    def __init__(self, size=0):
        """constructor:
           Args:
               size: int is a must
            Raise:
                TypeError: size must be an integer
                ValueError: size < 0
                """
        if is not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Returns: size squared"""

        return self.__size ** 2

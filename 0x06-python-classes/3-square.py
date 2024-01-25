#!/usr/bin/python3
"""square"""


class Square:
    """defining a square"""

    def __init__(self, size=0):
        """
        initialization:
           Square size

           Args:
               size: int is a must
            Raise:
                TypeError: size must be an integer
                ValueError: size < 0
            Returning: None
                """

        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Returns: size squaried"""

        return self.__size * self.__size

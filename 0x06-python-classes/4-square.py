#!/usr/bin/python3

class Square:
    """creating a class"""

    def __init__(self, size=0):
        """
        init:
           size
        Raises:
        2 Errors

        return: None
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def size(self):
        return self.__size

    def size(self, value):
        if is not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        return self.__size * self.__size

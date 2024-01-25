#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("Not an int")
        if size < 0:
            raise ValueError("not okay")
        self.__size = size

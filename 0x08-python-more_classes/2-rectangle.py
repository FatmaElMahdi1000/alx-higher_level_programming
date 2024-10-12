#!/usr/bin/python3
"""
Creating Rectangle class

claculating area and perimeter
"""


class Rectangle:
    """
    Rectangle class
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        result1 = int(self.__width * self.__height)
        return result1

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            result2 = (2 * self.__width) + (self.__height * 2)
           return result2

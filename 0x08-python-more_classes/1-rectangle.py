#!/usr/bin/python3
"""
Rectangle class
"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):

        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(width, int):
            if width < 0:
                raise ValueError("width must be >= 0")
            else:
                raise TypeError("width must be an integer")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(height, int):
            if width < 0:
                raise ValueError("height must be >= 0")
            else:
                raise TypeError("height must be an integer")

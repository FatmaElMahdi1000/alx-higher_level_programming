#!/usr/bin/python3
"""

class Rectangle that defines a rectangle

"""


class Rectangle:
    """
    A class to represent a rectangle.

    Attributes:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.
    number_of_instances (int): The number of instances of Rectangle.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @propert
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        result = self.__width * self.__height
        return result

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if (self.__width == 0 or self.__height == 0):
            return 0
        else:
            result = (2 * self.__width) + (2 * self.__height)
            return result

    def __str__(self):
        """Return a string representation of the rectangle using '#' """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rows = []
            for _ in range(self.__height):
                rows.append("#" * self.__width)
                return "\n".join(rows)

    def __repr__(self):
        """Return a string representation of the rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message when a rect. instance is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

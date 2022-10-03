#!/usr/bin/python3
"""Definition of a class Rectangle"""


class Rectangle:
    """Declaration of the instance attributes"""

    def __init__(self, width=0, height=0):
        """declaration of attributes of rectangle

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            print()
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                print("#", end="")
            print()

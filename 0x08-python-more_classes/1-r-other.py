#!/usr/bin/python3
"""Declaration of a class Rectangle"""


class Rectangle:
    """Declaration of instance attributes"""

    def __init__(self, width=0, height=0):
        """Creation of instance of Rectangle

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
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

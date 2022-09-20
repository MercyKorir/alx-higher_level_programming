#!/usr/bin/python3
"""Definition of class Rectangle"""


class Rectangle:
    """Contains the attributes of a rectangle"""

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    def width(self):
        return self.__width

    def width(self, value):
        self.__width = value
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 9")

    def height(self):
        return self.__height

    def height(self, value):
        self.__height = value
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

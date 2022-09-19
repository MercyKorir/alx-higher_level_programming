#!/usr/bin/python3
"""Definition of class Rectangle"""


class Rectangle:
    """Contains the attributes of a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize new object"""
        self.__height = height
        self.__width = width
    def width(self):
        return self.width
    def width(self, value):
        self.width = value
        result = isinstance(value, int)
        if result == False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 9")
    def height(self):
        return self.height
    def height(self, value):
        self.height = value
        res = isinstance(value, int)
        if res == False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

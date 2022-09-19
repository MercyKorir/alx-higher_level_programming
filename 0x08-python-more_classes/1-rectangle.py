#!/usr/bin/python3
"""Definition of class Rectangle"""


class Rectangle:
    """Contains the attributes of a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize new object

        Args:
            width (int): Width of object
            height (int): Height of new object
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """gets width"""
        return self.width

    @width.setter
    def width(self, value):
        self.width = value
        result = isinstance(value, int)
        if result == False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 9")

    @property
    def height(self):
        """Gets height"""
        return self.height

    @height.setter
    def height(self, value):
        self.height = value
        res = isinstance(value, int)
        if res == False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

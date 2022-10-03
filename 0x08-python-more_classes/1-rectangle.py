#!/usr/bin/python3
"""Definition of class Rectangle"""


class Rectangle:
    """Contains the attributes of a rectangle"""

    def __init__(self, width=0, height=0):
        """Declaration of attributes height and width

        Args:
            height (int): height of the rectangle
            width (int): width of the rectangle
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

#!/usr/bin/python3
"""Definition of class Rectangle"""
class Rectangle:
    """Attributes of a rectangle"""
    def __init(self, width=0, height=0):
        self.__width = width
        self.__height = height
    def width(self):
        return self.__width
    def width(self, value):
        self.__width = value
        result = isinstance(value, int)
        if result == False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
    def height(self):
        return self.__height
    def height(self, value):
        self.__height = value
        res = isinstance(value, int)
        if res == False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
    def area(self):
        return self.__width * self.__height
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__width + self.__height + self.__width + self.__height
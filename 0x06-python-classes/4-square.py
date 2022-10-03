#!/usr/bin/python3
"""Definition of a class Square"""


class Square:
    """Declaration of instance variables and methods"""

    def __init__(self, size=0):
        """Instantiating the class Square

        Args:
            size (int): the size of the square
        """
        self.__size = size

    @property
    def size(self):
        return (self.__width)

    @size.setter
    def size(self, value):
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return (self.__size * self.__size)

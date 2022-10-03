#!/usr/bin/python3
"""Defintion of the class Square"""


class Square:
    """Declarations of instance variables and methods"""

    def __init__(self, size=0):
        """Initialization of class Square

        Args:
            size (int): size of the square
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size myst be >= 0")
    def area(self):
        return (self.__size * self.__size)

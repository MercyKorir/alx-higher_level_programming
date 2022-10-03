#!/usr/bin/python3
"""Defintion of a class Square"""


class Square:
    """Declaration of the private attribute size"""

    def __init__(self, size=0):
        """Initializes the class

        Args:
            size (int): size of square
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

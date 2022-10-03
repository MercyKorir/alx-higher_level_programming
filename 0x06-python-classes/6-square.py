#!/usr/bin/python3
"""Definition of a class Square"""


class Square:
    """Declaration of instance variables and methods"""

    def __init__(self, size=0, position=(0, 0)):
        """Instantiating the class Square

        Args:
            size (int): the size of the square
            position (tuple): the position of the square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        self.__position = value
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        for item in value:
            if not isinstance(item, int) or item < 0:
                raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print()
        if self.__position[1] > 0:
            for i in range(0, self.__position[1]):
                print()
        for i in range(0, self.__size):
            for k in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print()

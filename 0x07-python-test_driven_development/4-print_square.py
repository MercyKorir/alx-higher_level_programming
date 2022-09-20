#!/usr/bin/python3
"""Definition of a function that prints a square"""


def print_square(size):
    """The user inputs size of square and it is
    printed using character #
    """

    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) is True and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

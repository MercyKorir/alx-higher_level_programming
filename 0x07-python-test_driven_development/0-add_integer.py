#!/usr/bin/python3
"""Definition of a function that computes sum"""


def add_integer(a, b=98):
    """This function returns the sum of a and b
    The function raises a type error if either a or b
    is not integer
    """

    if isinstance(a, int) is False and isinstance(a, float) is False:
        raise TypeError("a must be an integer")
    if isinstance(b, int) is False and isinstance(b, float) is False:
        raise TypeError("b must be an integer")
    if isinstance(a, float) is True:
        a = int(a)
    if isinstance(b, float) is True:
        b = int(b)
    sum = a + b
    return sum

#!/usr/bin/python3
"""Definition of function that prints name"""
def say_my_name(first_name, last_name=""):
    """First name and last name input is taken and full name
    printed as output
    """
    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

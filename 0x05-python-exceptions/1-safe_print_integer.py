#!/usr/bin/python3
def safe_print_integer(value):
    isInt = isinstance(value, int)
    while True:
        try:
            print("{:d}".format(value))
            return (isInt)
        except ValueError:
            print("{} is not an integer".format(value))
            return (isInt)
        finally:
            break

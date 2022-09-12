#!/usr/bin/python3
def safe_print_integer(value):
    isInt = isinstance(value, int)
    while True:
        try:
            print("{:d}".format(value))
            return True
        except ValueError:
            print("{} is not an integer".format(value))
            return False
        finally:
            break

#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if b > a:
        sum = add(a, b)
        for i in range(4, 6):
            sum = add(sum, i)
        return sum
    else:
        diff = sub(a, b)
        return diff

#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    c = add(10, 5)
    d = sub(10, 5)
    e = mul(10, 5)
    f = div(10, 5)
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, c))
    print("{} - {} = {}".formar(a, b, d))
    print("{} * {} = {}".format(a, b, e))
    print("{} / {} = {}".format(a, b, f))

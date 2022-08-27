#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    print("\n".join(["".join(["{:4d}".format(x) for x in row]) for row in matrix]))

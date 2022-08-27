#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    row = len(matrix)
    for x in range(row):
        col = len(matrix[x])
        for y in range(col):
            if y == (col - 1):
                print("{:d}".format(matrix[x][y]), end="$\n")
            else:
                print("{:d}".format(matrix[x][y]), end=" ")

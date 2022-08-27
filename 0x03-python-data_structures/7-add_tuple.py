#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        for i in range(2):
            if len(tuple_a) != 2:
                tuple_a = tuple_a + (0,)
            else:
                break
    if len(tuple_a) > 2:
        tuple_a = tuple_a[:2]
    if len(tuple_b) < 2:
        for j in range(2):
            if len(tuple_b) != 2:
                tuple_b = tuple_b + (0,)
            else:
                break
    if len(tuple_b) > 2:
        tuple_b = tuple_b[:2]
    tuple_sum = tuple(map(sum, zip(tuple_a, tuple_b)))
    return tuple_sum

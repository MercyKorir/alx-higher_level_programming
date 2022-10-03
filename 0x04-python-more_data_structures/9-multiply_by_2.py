#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    dict_cpy = dict(a_dictionary)
    for i in dict_cpy:
        dict_cpy[i] *= 2
    return (dict_cpy)

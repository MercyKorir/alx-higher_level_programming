#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    my_list.reverse()
    for x in my_list:
        print("{:d}".format(my_list[x]))

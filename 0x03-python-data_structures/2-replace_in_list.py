#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    length = len(my_list)
    if idx < 0:
        return my_list
    if idx > length:
        return my_list
    for x in range(length):
        if x == idx:
            my_list[x] = element
    return my_list

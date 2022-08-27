#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)
    list = my_list.copy()
    if idx < 0:
        return list
    if idx > length:
        return list
    for x in range(len(list)):
        if x == idx:
            list[x] = element
    return list

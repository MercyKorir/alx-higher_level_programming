#!/usr/bin/python3

def search_replace(my_list, search, replace):
    length = len(my_list)
    new_list = my_list[:]
    for element in range(length):
        if element == search:
            element = replace
        else:
            element = element
    return (new_list)

#!/usr/bin/python3

def search_replace(my_list, search, replace):
    for element in my_list:
        if element == search:
            element = replace
        else:
            element = element

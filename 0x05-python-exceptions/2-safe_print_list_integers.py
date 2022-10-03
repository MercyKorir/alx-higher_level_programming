#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    length = len(my_list[:x])
    count = 0

    for i in range(length):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            break
    return (count)

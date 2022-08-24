#!/usr/bin/python3
def remove_char_at(str, n):
    final_str = ""
    for i in range(0, len(str)):
        if i != n:
            final_str = final_str + str[i]
    return final_str

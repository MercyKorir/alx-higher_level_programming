#!/usr/bin/python3

def roman_to_int(roman_string):
    i = 0
    int_val = 0

    if not isinstance(roman_string, str):
        return (0)
    if roman_string is None:
        return (0)
    roman_values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000}
    while i < len(roman_string):
        if i + 1 < len(roman_string) and roman_string[i:i+2] in roman_values:
            int_val += roman_values[roman_string[i:i+2]]
            i += 2
        else:
            int_val += roman_values[roman_string[i]]
            i += 1
    return (int_val)

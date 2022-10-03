#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        best_score = None
    else:
        best_score = max(a_dictionary, key=a_dictionary.get)
    return (best_score)

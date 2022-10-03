#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) is 0:
        best_score = None
    best_score = max(a_dictionary, key=a_dictionary.get)
    return (best_score)

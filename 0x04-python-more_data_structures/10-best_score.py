#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    best_score = max(a_dictionary.values())
    return (best_score)

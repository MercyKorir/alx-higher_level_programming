#!/usr/bin/python3
"""Definition of the function text_identation"""


def text_identation(text):
    """function prints text with 2 new lines after each
    . ? and : character
    """

    i = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    while i < len(text) and text[i] == " ":
        i += 1
    while i < len(text):
        print(text[i], end="")
        if text[i] == "\n" or text[i] in ".?:":
            if text[i] in ".?:":
                print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        c += 1

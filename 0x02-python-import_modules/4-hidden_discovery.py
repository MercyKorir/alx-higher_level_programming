#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    all_names = dir(hidden_4)
    for name in all_names:
        if name[0:2] == "__":
            continue
        print(name):

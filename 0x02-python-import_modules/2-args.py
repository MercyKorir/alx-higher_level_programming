#!/usr/bin/python3
import sys
if __name__ == "__main__":
    len = len(sys.argv)
    if len == 1:
        print("{} arguments.".format(len - 1))
    elif len == 2:
        print("{} argument:".format(len - 1))
        for i in range(len - 1):
            print("{}: {}".format(i, sys.argv[i]))
    else:
        print("{} arguments:".format(len - 1))
        for i in range(len - 1):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))

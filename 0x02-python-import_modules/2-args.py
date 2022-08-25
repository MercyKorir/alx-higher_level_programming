#!/usr/bin/python3
import sys
len = len(argv)
if len == 0:
    print("{} arguments.".format(len))
elif len == 1:
    print("{} argument:".format(len))
    for i in argv[]:
        print("{}: {}".format(i, argv[i]))
else:
    print("{} arguments:".formtat(len))
    for i in argv[]:
        print("{}: {}".format(i, argv[i]))

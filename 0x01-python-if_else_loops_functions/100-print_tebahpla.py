#!/usr/bin/python3
lower = 1
upper = 0
for l in range(122, 97, -2):
    print("{:s}{:s}".format(chr(l), chr(l - 33)), end="")

#!/usr/bin/python3
for l in range(122, 97, -2):
    print("{:s}{:s}".format(chr(l), chr(l - 33)), end="")

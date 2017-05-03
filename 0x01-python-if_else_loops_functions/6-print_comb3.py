#!/usr/bin/python3
for a in range(0, 10):
    for b in range(0, 10):
        if a != b and a < b and a != 8:
            print("{:d}{:d}, ".format(a, b), end="")
        elif a != b and a < b and a == 8:
            print("{:d}{:d}\n".format(a, b), end="")

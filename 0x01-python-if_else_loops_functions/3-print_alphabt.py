#!/usr/bin/python3
for l in range(97, 123):
    if chr(l) != 'q' and chr(l) != 'e':
        print("{:s}".format(chr(l)), end="")

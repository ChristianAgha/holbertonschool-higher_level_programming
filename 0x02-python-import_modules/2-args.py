#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) is 1:
        print("0 argument.")

    elif len(sys.argv) is 2:
        print("1 argument:\n1: {:s}".format(sys.argv[1]))

    else:
        print("{:d} arguments:".format(len(sys.argv) - 1))

        for n in range(1, len(sys.argv)):
            print("{:d}: {:s}".format(n, sys.argv[n]))

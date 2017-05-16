#!/usr/bin/python3
"""
This module contains the print_square function that prints
squares of #s depending on the size it is given
"""


def print_square(size):
    """
    This function takes the size input and makes a square of #s
    with size 'size', it also makes sure that size is a positive
    integer and raises an error otherwise
    """
    if isinstance(size, int) and size >= 0:
        for i in range(size):
            for j in range(size - 1):
                print("#", end="")
            print("#")
    elif size < 0 and isinstance(size, int):
        raise ValueError("size must be >= 0")
    else:
        raise TypeError("size must be an integer")

#!/usr/bin/python3
"""
add_integer module takes 2 numbers as inputs and returns the result of their
addition. It raises a TypeError if either of the inputs is not an int or float.
"""


def add_integer(a, b):
    """
    add_integer module takes 2 numbers as inputs and returns the result of
    their addition. It raises a TypeError if either of the inputs is not
    an int or a float.
    """
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return (int(a) + int(b))
    else:
        if not isinstance(a, (int, float)):
            raise TypeError("a must be an integer")
        if not isinstance(b, (int, float)):
            raise TypeError("b must be an integer")

#!/usr/bin/python3
"""
This module contains a funcation 'say_my_name' that returns a string
in the format 'My name is first_name last_name'
"""


def say_my_name(first_name, last_name=""):
    """
    This functions returns a string in the format 'my name is
    first_name last_name'. It also checks to make sure the input
    is valid.
    """
    if isinstance(first_name, str) and isinstance(last_name, str):
        print("{} {} {}".format("My name is", first_name, last_name))
    elif not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

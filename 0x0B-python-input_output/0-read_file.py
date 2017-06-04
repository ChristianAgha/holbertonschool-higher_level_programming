#!/usr/bin/python3
"""Read file module"""


def read_file(filename=""):
    """a function that reads a text file and prints it to stdout"""
    with open(filename, encoding='utf-8') as a_file:
        print(a_file.read(), end='')

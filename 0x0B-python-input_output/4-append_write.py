#!/usr/bin/python3
"""Append to a file module"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file
    and returns the number of characters added"""
    with open(filename, mode='a', encoding='utf-8') as a_file:
        a_file.write(text)
    return len(text)

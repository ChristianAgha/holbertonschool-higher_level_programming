#!/usr/bin/python3
"""Write to a file module"""


def write_file(filename="", text=""):
    """writes string to text file & returns the number of characters written"""
    with open(filename, mode='w', encoding='utf-8') as a_file:
        a_file.write(text)

    return len(text)

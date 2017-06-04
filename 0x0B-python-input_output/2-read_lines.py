#!/usr/bin/python3
"""Read n lines module"""


def read_lines(filename="", nb_lines=0):
    """a function that reads n lines of a text file"""
    with open(filename, encoding='utf-8') as a_file:
        if nb_lines > 0:
            lines = a_file.readlines()
            for i in range(nb_lines):
                print(lines[i], end='')
        else:
            print(a_file.read(), end='')

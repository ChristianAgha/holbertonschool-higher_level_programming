#!/usr/bin/python3
"""number_of_lines module"""


def number_of_lines(filename=""):
    """returns the number of lines of a text file"""
    line_num = 0
    with open(filename, encoding='utf-8') as a_file:
        for a_line in a_file:
            line_num += 1
    return line_num

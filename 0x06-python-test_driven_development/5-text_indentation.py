#!/usr/bin/python3
"""
This module contains a function 'text_indentation' that prints
text it's given and adds 2 \n charachters after any ., ?, and :
"""


def text_indentation(text):
    """
    This functions takes text input and prints it out but adding 2 \n
    charachters after every ., ? and :. It also raises an error if the
    input was not a string.
    """
    special_chars = ['.', '?', ':']
    skip_front_space = 0
    if isinstance(text, str):
        for i, char in enumerate(text):
            if skip_front_space == 0 and char == ' ':
                continue
            skip_front_space = 1
            if char == ' ' and text[i - 1] not in special_chars:
                print(char, end='')
            if char != ' ':
                print(char, end='')

            if char in special_chars:
                print('\n\n', end='')
                skip_front_space = 0
    else:
        raise TypeError("text must be a string")

#!/usr/bin/python3
"""returns the list of available attributes"""


def lookup(obj):
    return list(dir(obj))

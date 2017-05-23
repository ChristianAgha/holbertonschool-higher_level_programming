#!/usr/bin/python3
"""Square class """


class Square:
    """Square class"""
    def __init__(self, size=0):
        if isinstance(size, int):
            if size >= 0:
                self._Square__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

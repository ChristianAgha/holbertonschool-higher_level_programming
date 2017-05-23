#!/usr/bin/python3
"""Square class """


class Square:
    """Square class"""
    def __init__(self, size=0):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            print("this is not an int!!!!!!!!!")
            raise TypeError("size must be an integer")

    # This is the getter
    @property
    def size(self):
        return self.__size

    # This is the setter
    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    # function that returns area
    def area(self):
        return (self.__size * self.__size)

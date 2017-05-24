#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Rectangle class definition"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """width property"""
        return(self.__width)

    @property
    def height(self):
        """height property"""
        return(self.__height)

    @width.setter
    def width(self, value):
        "sets the width to input value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        "sets the height to input value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return(self.__width * self.__height)

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return(0)
        return(self.__width * 2 + self.__height * 2)

    def __str__(self):
        """prints the rectangle with the character #"""
        hash_rectangle = "{}".format('\n'.join("#" * self.__width for i in range(0, self.__height)))
        return hash_rectangle

    def __repr__(self):
        """returns a string representation of the rectangle dimentions"""
        return("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """called when a Rectangle instance is deleted"""
        print("Bye rectangle...")

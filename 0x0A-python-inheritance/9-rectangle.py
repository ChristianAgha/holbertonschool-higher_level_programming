#!/usr/bin/python3
"""Geometry Module"""


class BaseGeometry:
    """class BaseGeometry"""
    def area(self):
        """raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """class Rectangle"""
    def __init__(self, width, height):
        """initialization"""
        self.__width__ = width
        self.__height__ = height
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)

    def __str__(self):
        """for print"""
        return("[Rectangle] {}/{}".format(self.__width__, self.__height__))

    def area(self):
        """return area"""
        return self.__width__ * self.__height__

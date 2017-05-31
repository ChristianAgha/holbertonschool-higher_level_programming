#!/usr/bin/python3
"""My Integer Module"""


class MyInt(int):
    """MyInt class"""

    def __init__(self, num1):
        """initialization"""
        self.__num1 = num1

    def __eq__(self, num2=0):
        """overriding =="""
        if (self.__num1 == num2):
            return False
        else:
            return True

    def __ne__(self, num2):
        """overriding !="""
        if (self.__num1 == num2):
            return True
        else:
            return False

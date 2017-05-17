#!/usr/bin/python3
"""
This module contains function matrix_divided that takes in a matrix of
numbers and returns a new matrix with all the numbers divided on the div
number matrix_divided takes in
"""


def matrix_divided(matrix, div):
    """
    This function takes in a matrix of numbers and a divisor
    and returns a new matrix whos numbers are numbers of the
    original matrix divided by the divisor. The functions checkes
    to make sure it is getting the correct input and raises errors
    if the wrong input is given
    """
    matrix_Size = len(matrix[0])
    div_list = []

    for col in range(len(matrix)):
        for row in range(len(matrix[col])):
            if not isinstance(matrix[col][row], (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for s in range(len(matrix)):
        if len(matrix[s]) != matrix_Size:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for x in matrix:
        div_list.append(list(map(lambda x: round(x / div, 2), x)))

    return div_list

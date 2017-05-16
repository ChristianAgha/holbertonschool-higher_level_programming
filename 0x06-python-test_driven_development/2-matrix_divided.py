#!/usr/bin/python3
"""

"""


def matrix_divided(matrix, div):
    """
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

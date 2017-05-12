#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squareList = []
    for x in matrix:
        squareList.append(list(map(lambda x: x ** 2, x)))
    return squareList

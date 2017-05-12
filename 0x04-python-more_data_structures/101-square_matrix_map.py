#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda in_L: list(map(lambda x: x ** 2, in_L)), matrix)))

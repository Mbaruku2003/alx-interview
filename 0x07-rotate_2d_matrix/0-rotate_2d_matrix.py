#!/usr/bin/python3
"""Define the function."""


def rotate_2d_matrix(matrix):
    """we will rotate a 2d matrix."""

    for x, y in enumerate(zip(*reversed(matrix))):
        matrix[x] = list(y)

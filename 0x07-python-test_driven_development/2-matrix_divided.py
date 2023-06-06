#!/usr/bin/python3
# 2-matrix_divided.py
"""Definesa function that divides every element of a matrix"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.
    Args:
       matrix(list) = list of lists of integers or floats
       div(int or float) = divisor
    Raises:
       TypeError: if matrix is not list of lists of integers or floats
       TypeError: if rows of matrix not of the same size
       TypeError: if div is not a number
       ZeroDivisionError: if div is Zero
    Returns:
       A new matrix
    """
    sizeErr = "Each row of the matrix must have the same size"
    typeErr = "matrix must be a matrix (list of lists) of integers/floats"

    if matrix == [] or matrix is None:
        raise TypeError(typeErr)

    if not all(isinstance(row, list) for row in matrix) or (
            not all(all(isinstance(num, (int, float)) for num in row) for
                    row in matrix)):
        raise TypeError(typeErr)

    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError(sizeErr)

    if not (isinstance(div, (int, float))):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return (new_matrix)

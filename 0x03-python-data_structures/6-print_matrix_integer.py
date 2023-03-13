#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    '''prints a matrix of integers'''

    for row in matrix:
        for num in row:
            print("{:d}".format(num), end=" " if numb != row[-1] else "")
        print()

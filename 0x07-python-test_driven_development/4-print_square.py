#!/usr/bin/python3
# 4-print_square.py
"""Defines a function that prints a square."""


def print_square(size):
    """Prints a square. Uses the character '#'.

    Args:
        size(int) = length of square

    Raises:
        TypeError: if size is not an integer
        TypeError: if size is a float and less than 0
        ValueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)

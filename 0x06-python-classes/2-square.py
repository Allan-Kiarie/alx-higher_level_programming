#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """A representation of object square"""

    def __init__(self, size=0):
        """Initialization of a new Square.

        Args:
            size(int): size of the new Square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

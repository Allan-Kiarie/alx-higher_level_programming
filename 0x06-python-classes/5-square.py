#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """A representation of object square"""

    def __init__(self, size=0):
        """Initialization of a new Square.

        Args:
            size(int): size of the new Square.
        """
        self.size = size

    @property
    def size(self):
        """Access the attribute size in class Square"""
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns area of current square"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
            return

        for i in range(self.__size):
            print("#" * self.__size)

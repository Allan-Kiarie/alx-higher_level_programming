#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """A representation of object square"""

    def __init__(self, size=0, position=(0,0)):
        """Initialization of a new Square.

        Args:
            size(int): size of the new Square.
            position(int, int): starting co-ordinate of the new Square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Access the attribute size in class Square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get or set the co-ordinates of the new square"""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
        len(value) != 2 or
        not isinstance(value[0], int) or
        not isinstance(value[1], int) or
        value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns area of current square"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

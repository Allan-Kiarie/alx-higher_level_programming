#!/usr/bin/python3
"""Defines a class Square that inherits from class Rectangle"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """A representation of the object square"""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size(int): Length of square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """print the object Square using print() and str()"""
        my_string = "[Square] " + str(self.__size) + "/" + str(self.__size)

        return (my_string)

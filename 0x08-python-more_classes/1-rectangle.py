#!/usr/bin/python3
# 0-rectangle.py
"""Defines a class 'rectangle'"""


class Rectangle:
    """A representation of class rectangle"""
    
    def __init__(self, width=0, height=0):
        """Initializing a new rectangle.

        Args:
            width(int): The width of the rectangle
            height(int): The height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Access attribute width in class Rectangle

        Raises:
            TypeError: if not integer
            ValueError: if width less than zero
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Access attribute height in class Rectangle.

        Raises:
            TypeError: if height not an integer
            ValueError: if height is less than zero
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        elif value < 0:
            raise ValueError("height must be >= 0")
        
        else:
            self.__height = value

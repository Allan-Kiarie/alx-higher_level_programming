#!/usr/bin/python3
# 5-base_geometry.py
"""Defines a class BaseGeometry."""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A representation of the object rectangle"""

    def __init__(self, width, height):
        """Initializes a new rectangle.

        Args:
            width(int): width of rectangle
            height(int): length of the rectangle
        """
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)

    def area(self):
        """Returns area of the object rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Print a representation of the object rectangle"""
        my_str = "[Rectangle] " + str(self.__width) + "/" + str(self.__height)

        return my_str

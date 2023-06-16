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
        self.integer_validator("width", width)
        self.integer_validator("height", height)

#!/usr/bin/python3
# 5-base_geometry.py
"""Defines a class BaseGeometry."""


class BaseGeometry:
    """A representation of the object BaseGeometry"""

    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates that a parameter is an integer.

        Args:
            name(str): name of the parameter
            value(int): parameter to be validated
        Raises:
            TypeError: if value not an integer
            ValueError: value less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")

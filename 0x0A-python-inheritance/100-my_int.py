#!/usr/bin/python3
"""Defines a class MyInt that inherits from int"""


class MyInt(int):
    """A representation of object MyInt that inverts '==' and
    '!=' operators
    """
    def __eq__(self, value):
        """Overide the __eq__ method with __ne__"""
        return super().__ne__(value)

    def __ne__(self, value):
        """Overide the __ne__ method with __eq__"""
        return super().__eq__(value)

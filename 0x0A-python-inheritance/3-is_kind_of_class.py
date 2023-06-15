#!/usr/bin/python3
# 3-is_kind_of_class.py
"""Defines a function that checks if object is instance of a class"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False.

    Args:
        obj(any): Input object
        a_class(type): class to match the type of obj
    """
    if isinstance(obj, a_class):
        return True
    return False

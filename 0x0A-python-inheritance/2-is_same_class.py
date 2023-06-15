#!/usr/bin/python3
# 2-is_same_class.py
"""Defines a function that checks the type of object"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of the specified class
    otherwise False.

    Args:
        obj: input object
        a_class: class
    """
    return (type(obj) is a_class)

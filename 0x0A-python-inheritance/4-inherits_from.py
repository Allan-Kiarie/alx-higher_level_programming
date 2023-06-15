#!/usr/bin/python3
# 4-inherits_from.py
"""Defines a function that checks if obj is a subclass"""


def inherits_from(obj, a_class):
    """Checks if an obj is an instance of a class
    that inherited from the specified class.

    Args:
        obj(any): input obj
        a_class(type): parent class for obj to be matched to

    Returns:
        True: if obj is instance of a child of a_class
        False: if otherwise
    """
    if issubclass(obj.__class__, a_class) and obj.__class__ != a_class:
        return True
    return False

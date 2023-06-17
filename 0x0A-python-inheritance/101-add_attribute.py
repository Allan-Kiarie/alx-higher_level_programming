#!/usr/bin/python3
"""Defines a function that tries to add a new attribute to an object"""


def add_new_attribute(obj, attr_name, attr_value):
    """Adds a new attribute to an object if it’s possible.

    Args:
        Obj(any): object to add att. to
        attr_name(str): name of att. to be added
        attr_value(any): value of the att.
    Raises:
        TypeError: if att. cannot be added
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    obj.__dict__[attr_name] = attr_value

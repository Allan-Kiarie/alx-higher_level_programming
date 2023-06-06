#!/usr/bin/python3
"""Defines a function that adds two integers.
Raises an error for non-integer values
"""


def add_integer(a, b=98):
    """Returns the sum of a and b.

    args:
        a (int or float) = first parameter
        b (int or float) = second parameter

    Returns:
        a + b

    Floats typecasted to integers before addition
    Raises:
        TypeError: if a or b is neither int nor float
    """
    if (not isinstance(a, (int, float))):
        raise TypeError("a must be an integer")

    if (not isinstance(b, (int, float))):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
